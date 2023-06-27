/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include <type_traits>

#include <Python.h>
#include <folly/CppAttributes.h>
#include <folly/Traits.h>
#include <folly/Utility.h>
#include <thrift/lib/cpp2/FieldRefTraits.h>
#include <thrift/lib/python/capi/types.h>
#include <thrift/lib/python/types.h>

namespace apache {
namespace thrift {
namespace python {
namespace capi {
/**
 * Series of functions to convert a native type T into a Python object
 *
 * Some important notes:
 * 1. The construct function returns a 'new reference'. i.e. you own the object
 *    it returns.
 * 2: The constructor will leave the python indicator set if a python
 *    exception is encountered during the extraction. Be sure to check the error
 *    indicator before calling back into python!
 */
template <typename T>
struct Constructor {
  template <typename U>
  struct Unspecialized : std::false_type {};
  static_assert(Unspecialized<T>{}, "No constructor defined");
  /* Target */ PyObject* operator()(T&&);
};

/**
 * CRTP helper to handle FieldRef appropriately and call `Constructor` from
 * the field's cpp value. Returns nullptr to signal python error. Otherwise
 * returns a new reference.
 */
template <typename T>
struct BaseConstructor {
  template <typename FieldRef>
  std::enable_if_t<
      !::apache::thrift::detail::is_shared_or_unique_ptr_v<FieldRef>,
      PyObject*>
  constructFrom(FieldRef ref) {
    if constexpr (is_optional_maybe_boxed_field_ref_v<FieldRef>) {
      if (!ref.has_value()) {
        Py_RETURN_NONE;
      }
    }
    return (*static_cast<Constructor<T>*>(this))(std::move(*ref));
  }
  template <typename S>
  PyObject* constructFrom(std::unique_ptr<S>& ref /* RefType.Unique */
  ) {
    // Ref may be optional so always check if None
    if (!ref) {
      Py_RETURN_NONE;
    }
    return (*static_cast<Constructor<T>*>(this))(std::move(*ref));
  }
  template <typename S>
  PyObject* constructFrom(
      std::shared_ptr<S>& ref /* RefType.Shared, RefType.SharedMutable */
  ) {
    // Ref may be optional so always check if None
    if (!ref) {
      Py_RETURN_NONE;
    }
    // have to copy because we can't guarantee shared_ptr is unique in general
    // multi-threaded case.
    return (*static_cast<Constructor<T>*>(this))(folly::copy(*ref));
  }
};

#define SPECIALIZE_SCALAR(type)                             \
  template <>                                               \
  struct Constructor<type> : public BaseConstructor<type> { \
    PyObject* FOLLY_NULLABLE operator()(type&&);            \
  }

SPECIALIZE_SCALAR(int8_t);
SPECIALIZE_SCALAR(int16_t);
SPECIALIZE_SCALAR(int32_t);
SPECIALIZE_SCALAR(int64_t);
SPECIALIZE_SCALAR(uint32_t);
SPECIALIZE_SCALAR(uint64_t);
SPECIALIZE_SCALAR(bool);
SPECIALIZE_SCALAR(float);
SPECIALIZE_SCALAR(double);

#undef SPECIALIZE_SCALAR
#define SPECIALIZE_STR(cpp_type, py_type)                         \
  template <>                                                     \
  struct Constructor<py_type> : public BaseConstructor<py_type> { \
    PyObject* FOLLY_NULLABLE operator()(cpp_type&&);              \
  }

SPECIALIZE_STR(std::string, Bytes);
SPECIALIZE_STR(std::string, String);

#undef SPECIALIZE_STR

template <typename T>
struct Constructor<ComposedEnum<T>> : public BaseConstructor<ComposedEnum<T>> {
  // The internal python representation of enum is integer value.
  PyObject* FOLLY_NULLABLE operator()(T&& val) {
    return Constructor<int32_t>{}(static_cast<int32_t>(val));
  }
};

template <typename ElemT, typename CppT>
struct Constructor<list<ElemT, CppT>>
    : public BaseConstructor<list<ElemT, CppT>> {
  PyObject* FOLLY_NULLABLE operator()(CppT&& val) {
    const size_t size = val.size();
    StrongRef list(PyTuple_New(size));
    if (!list) {
      return nullptr;
    }
    Constructor<ElemT> ctor{};
    for (size_t i = 0; i < size; ++i) {
      // PyTuple_SET_ITEM steals, so don't use StrongRef
      PyObject* elem(ctor(std::move(val[i])));
      if (elem == nullptr) {
        // StrongRef DECREFs the list tuple on scope exit
        return nullptr;
      }
      PyTuple_SET_ITEM(*list, i, elem);
    }
    return std::move(list).release();
  }
};

template <typename C>
using iter_t = decltype(std::declval<C&>().begin());
template <typename C>
using extract_method_t =
    decltype(std::declval<C&>().extract(std::declval<iter_t<C>>()));
template <typename C>
constexpr bool has_extract_v =
    folly::is_detected_v<extract_method_t, std::remove_reference_t<C>>;

template <typename ElemT, typename CppT>
struct Constructor<set<ElemT, CppT>>
    : public BaseConstructor<set<ElemT, CppT>> {
  PyObject* FOLLY_NULLABLE operator()(CppT&& val) {
    StrongRef set_obj(PyFrozenSet_New(nullptr));
    if (!set_obj) {
      return nullptr;
    }
    Constructor<ElemT> ctor{};
    auto it = val.begin();
    while (it != val.end()) {
      StrongRef elem;
      if constexpr (has_extract_v<CppT>) {
        auto node_handle = val.extract(it++);
        elem = StrongRef(ctor(std::move(node_handle.value())));
      } else {
        // If the container doesn't support extract, have to copy
        // because set iterator is const :(
        elem = StrongRef(ctor(folly::copy(*it)));
        ++it;
      }
      if (*elem == nullptr) {
        // StrongRef DECREFs the frozenset on scope exit
        return nullptr;
      }
      // Not stolen, so let StrongRef DECREF on exit
      if (PySet_Add(*set_obj, *elem) == -1) {
        // Should only fail for MemoryError (OOM)
        return nullptr;
      }
    }
    return std::move(set_obj).release();
  }
};

template <typename KeyT, typename ValT, typename CppT>
struct Constructor<map<KeyT, ValT, CppT>>
    : public BaseConstructor<map<KeyT, ValT, CppT>> {
  PyObject* FOLLY_NULLABLE operator()(CppT&& cpp_map) {
    StrongRef dict(PyTuple_New(cpp_map.size()));
    if (!dict) {
      return nullptr;
    }
    Constructor<KeyT> key_ctor{};
    Constructor<ValT> val_ctor{};
    auto it = cpp_map.begin();
    size_t idx = 0;
    while (it != cpp_map.end()) {
      StrongRef key;
      StrongRef val;
      if constexpr (has_extract_v<CppT>) {
        auto node_handle = cpp_map.extract(it++);
        key = StrongRef(key_ctor(std::move(node_handle.key())));
        if (!key) {
          // StrongRef DECREFs the dict on scope exit
          return nullptr;
        }
        val = StrongRef(val_ctor(std::move(node_handle.mapped())));
      } else {
        // If the container doesn't support extract, have to copy
        // because set iterator is const :(
        key = StrongRef(key_ctor(folly::copy(it->first)));
        if (!key) {
          // StrongRef DECREFs the dict on scope exit
          return nullptr;
        }
        val = StrongRef(val_ctor(std::move(it->second)));
        ++it;
      }
      if (!val) {
        // StrongRef DECREFs the dict and key on scope exit
        return nullptr;
      }
      PyObject* kv_tuple = PyTuple_New(2);
      if (kv_tuple == nullptr) {
        return nullptr;
      }
      // PyTuple_SET_ITEM steals, so have to release StrongRefs
      PyTuple_SET_ITEM(kv_tuple, 0, std::move(key).release());
      PyTuple_SET_ITEM(kv_tuple, 1, std::move(val).release());
      PyTuple_SET_ITEM(*dict, idx++, kv_tuple);
    }
    return std::move(dict).release();
  }
};

} // namespace capi
} // namespace python
} // namespace thrift
} // namespace apache
