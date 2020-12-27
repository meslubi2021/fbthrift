/**
 * Autogenerated by Thrift for src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <thrift/lib/cpp2/visitation/visit_by_thrift_field_metadata.h>
#include "thrift/compiler/test/fixtures/any/gen-cpp2/module_metadata.h"

namespace apache {
namespace thrift {
namespace detail {

template <>
struct VisitByThriftId<::cpp2::MyStruct> {
  template <typename F, typename T>
  void operator()(FOLLY_MAYBE_UNUSED F&& f, size_t id, FOLLY_MAYBE_UNUSED T&& t) const {
    switch (id) {
    case 1:
      return f(0, static_cast<T&&>(t).myString_ref());
    default:
      throwInvalidThriftId(id, "::cpp2::MyStruct");
    }
  }
};

template <>
struct VisitByThriftId<::cpp2::MyUnion> {
  template <typename F, typename T>
  void operator()(FOLLY_MAYBE_UNUSED F&& f, size_t id, FOLLY_MAYBE_UNUSED T&& t) const {
    switch (id) {
    case 1:
      return f(0, static_cast<T&&>(t).myString_ref());
    default:
      throwInvalidThriftId(id, "::cpp2::MyUnion");
    }
  }
};

template <>
struct VisitByThriftId<::cpp2::MyException> {
  template <typename F, typename T>
  void operator()(FOLLY_MAYBE_UNUSED F&& f, size_t id, FOLLY_MAYBE_UNUSED T&& t) const {
    switch (id) {
    case 1:
      return f(0, static_cast<T&&>(t).myString_ref());
    default:
      throwInvalidThriftId(id, "::cpp2::MyException");
    }
  }
};
} // namespace detail
} // namespace thrift
} // namespace apache
