
/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT
 *  @generated
 *
 */

#pragma once

#include <thrift/lib/python/capi/constructor.h>
#include <thrift/lib/python/capi/extractor.h>

#include <thrift/compiler/test/fixtures/includes/src/gen-cpp2/includes_types.h>

namespace apache {
namespace thrift {
namespace python {
namespace capi {
template <>
struct Extractor<::cpp2::Included>
    : public BaseExtractor<::cpp2::Included> {
  ExtractorResult<::cpp2::Included> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Extractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Included>>
    : public BaseExtractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Included>> {
  ExtractorResult<::cpp2::Included> operator()(PyObject* obj);
};

template <>
struct Constructor<::cpp2::Included>
    : public BaseConstructor<::cpp2::Included> {
  PyObject* operator()(const ::cpp2::Included& val);
};

template <>
struct Constructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Included>>
    : public BaseConstructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Included>> {
  PyObject* operator()(const ::cpp2::Included& val);
};

} // namespace capi
} // namespace python
} // namespace thrift
} // namespace apache
