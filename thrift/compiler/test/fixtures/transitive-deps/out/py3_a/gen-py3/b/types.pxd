#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from libc.stdint cimport (
    int8_t as cint8_t,
    int16_t as cint16_t,
    int32_t as cint32_t,
    int64_t as cint64_t,
    uint32_t as cuint32_t,
)
from libcpp.string cimport string
from libcpp cimport bool as cbool, nullptr, nullptr_t
from cpython cimport bool as pbool
from libcpp.memory cimport shared_ptr, unique_ptr
from libcpp.vector cimport vector
from libcpp.set cimport set as cset
from libcpp.map cimport map as cmap, pair as cpair
from thrift.python.exceptions cimport cTException
cimport folly.iobuf as _fbthrift_iobuf
from thrift.py3.types cimport (
    bstring,
    field_ref as __field_ref,
    optional_field_ref as __optional_field_ref,
    required_field_ref as __required_field_ref,
    terse_field_ref as __terse_field_ref,
    union_field_ref as __union_field_ref,
    get_union_field_value as __get_union_field_value,
)
from thrift.python.common cimport cThriftMetadata as __fbthrift_cThriftMetadata
cimport c.types as _c_types
cimport thrift.py3.exceptions
cimport thrift.py3.types
from thrift.python.common cimport (
    RpcOptions as __RpcOptions,
    MetadataBox as __MetadataBox,
)
from folly.optional cimport cOptional as __cOptional

cimport b.types_fields as _fbthrift_types_fields

cdef extern from "thrift/compiler/test/fixtures/transitive-deps/gen-py3/b/types.h":
  pass







cdef class List__c_C(thrift.py3.types.List):
    cdef shared_ptr[vector[_c_types.cC]] _cpp_obj
    @staticmethod
    cdef _fbthrift_create(shared_ptr[vector[_c_types.cC]])
    @staticmethod
    cdef shared_ptr[vector[_c_types.cC]] _make_instance(object items) except *


