
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

#include <thrift/compiler/test/fixtures/constants/src/gen-cpp2/module_types.h>

namespace apache {
namespace thrift {
namespace python {
namespace capi {
template <>
struct Extractor<::cpp2::Internship>
    : public BaseExtractor<::cpp2::Internship> {
  ExtractorResult<::cpp2::Internship> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Extractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Internship>>
    : public BaseExtractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Internship>> {
  ExtractorResult<::cpp2::Internship> operator()(PyObject* obj);
};

template <>
struct Constructor<::cpp2::Internship>
    : public BaseConstructor<::cpp2::Internship> {
  PyObject* operator()(const ::cpp2::Internship& val);
};

template <>
struct Constructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Internship>>
    : public BaseConstructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Internship>> {
  PyObject* operator()(const ::cpp2::Internship& val);
};

template <>
struct Extractor<::cpp2::Range>
    : public BaseExtractor<::cpp2::Range> {
  ExtractorResult<::cpp2::Range> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Extractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Range>>
    : public BaseExtractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Range>> {
  ExtractorResult<::cpp2::Range> operator()(PyObject* obj);
};

template <>
struct Constructor<::cpp2::Range>
    : public BaseConstructor<::cpp2::Range> {
  PyObject* operator()(const ::cpp2::Range& val);
};

template <>
struct Constructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Range>>
    : public BaseConstructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::Range>> {
  PyObject* operator()(const ::cpp2::Range& val);
};

template <>
struct Extractor<::cpp2::struct1>
    : public BaseExtractor<::cpp2::struct1> {
  ExtractorResult<::cpp2::struct1> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Extractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct1>>
    : public BaseExtractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct1>> {
  ExtractorResult<::cpp2::struct1> operator()(PyObject* obj);
};

template <>
struct Constructor<::cpp2::struct1>
    : public BaseConstructor<::cpp2::struct1> {
  PyObject* operator()(const ::cpp2::struct1& val);
};

template <>
struct Constructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct1>>
    : public BaseConstructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct1>> {
  PyObject* operator()(const ::cpp2::struct1& val);
};

template <>
struct Extractor<::cpp2::struct2>
    : public BaseExtractor<::cpp2::struct2> {
  ExtractorResult<::cpp2::struct2> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Extractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct2>>
    : public BaseExtractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct2>> {
  ExtractorResult<::cpp2::struct2> operator()(PyObject* obj);
};

template <>
struct Constructor<::cpp2::struct2>
    : public BaseConstructor<::cpp2::struct2> {
  PyObject* operator()(const ::cpp2::struct2& val);
};

template <>
struct Constructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct2>>
    : public BaseConstructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct2>> {
  PyObject* operator()(const ::cpp2::struct2& val);
};

template <>
struct Extractor<::cpp2::struct3>
    : public BaseExtractor<::cpp2::struct3> {
  ExtractorResult<::cpp2::struct3> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Extractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct3>>
    : public BaseExtractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct3>> {
  ExtractorResult<::cpp2::struct3> operator()(PyObject* obj);
};

template <>
struct Constructor<::cpp2::struct3>
    : public BaseConstructor<::cpp2::struct3> {
  PyObject* operator()(const ::cpp2::struct3& val);
};

template <>
struct Constructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct3>>
    : public BaseConstructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct3>> {
  PyObject* operator()(const ::cpp2::struct3& val);
};

template <>
struct Extractor<::cpp2::struct4>
    : public BaseExtractor<::cpp2::struct4> {
  ExtractorResult<::cpp2::struct4> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Extractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct4>>
    : public BaseExtractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct4>> {
  ExtractorResult<::cpp2::struct4> operator()(PyObject* obj);
};

template <>
struct Constructor<::cpp2::struct4>
    : public BaseConstructor<::cpp2::struct4> {
  PyObject* operator()(const ::cpp2::struct4& val);
};

template <>
struct Constructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct4>>
    : public BaseConstructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::struct4>> {
  PyObject* operator()(const ::cpp2::struct4& val);
};

template <>
struct Extractor<::cpp2::union1>
    : public BaseExtractor<::cpp2::union1> {
  ExtractorResult<::cpp2::union1> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Extractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::union1>>
    : public BaseExtractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::union1>> {
  ExtractorResult<::cpp2::union1> operator()(PyObject* obj);
};

template <>
struct Constructor<::cpp2::union1>
    : public BaseConstructor<::cpp2::union1> {
  PyObject* operator()(const ::cpp2::union1& val);
};

template <>
struct Constructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::union1>>
    : public BaseConstructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::union1>> {
  PyObject* operator()(const ::cpp2::union1& val);
};

template <>
struct Extractor<::cpp2::union2>
    : public BaseExtractor<::cpp2::union2> {
  ExtractorResult<::cpp2::union2> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Extractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::union2>>
    : public BaseExtractor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::union2>> {
  ExtractorResult<::cpp2::union2> operator()(PyObject* obj);
};

template <>
struct Constructor<::cpp2::union2>
    : public BaseConstructor<::cpp2::union2> {
  PyObject* operator()(const ::cpp2::union2& val);
};

template <>
struct Constructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::union2>>
    : public BaseConstructor<::apache::thrift::python::capi::ComposedStruct<
        ::cpp2::union2>> {
  PyObject* operator()(const ::cpp2::union2& val);
};

template <>
struct Extractor<::cpp2::EmptyEnum>
    : public BaseExtractor<::cpp2::EmptyEnum> {
  ExtractorResult<::cpp2::EmptyEnum> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Constructor<::cpp2::EmptyEnum> {
  PyObject* operator()(::cpp2::EmptyEnum val);
};

template <>
struct Extractor<::cpp2::City>
    : public BaseExtractor<::cpp2::City> {
  ExtractorResult<::cpp2::City> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Constructor<::cpp2::City> {
  PyObject* operator()(::cpp2::City val);
};

template <>
struct Extractor<::cpp2::Company>
    : public BaseExtractor<::cpp2::Company> {
  ExtractorResult<::cpp2::Company> operator()(PyObject* obj);
  int typeCheck(PyObject* obj);
};

template <>
struct Constructor<::cpp2::Company> {
  PyObject* operator()(::cpp2::Company val);
};

} // namespace capi
} // namespace python
} // namespace thrift
} // namespace apache
