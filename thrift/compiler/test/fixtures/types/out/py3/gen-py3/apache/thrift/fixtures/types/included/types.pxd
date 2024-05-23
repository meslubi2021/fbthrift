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
cimport thrift.py3.exceptions
cimport thrift.py3.types
from thrift.python.common cimport (
    RpcOptions as __RpcOptions,
    MetadataBox as __MetadataBox,
)
from folly.optional cimport cOptional as __cOptional

cimport apache.thrift.fixtures.types.included.types_fields as _fbthrift_types_fields

cdef extern from "thrift/compiler/test/fixtures/types/gen-py3/included/types.h":
  pass

cdef extern from * nogil:
    cdef cppclass std_unordered_map "std::unordered_map"[T, U]:
        ctypedef T key_type
        ctypedef U mapped_type
        ctypedef size_t size_type

        cppclass iterator:
            cpair[T, U]& operator*()
            iterator operator++()
            bint operator==(iterator)
            bint operator!=(iterator)
        cppclass reverse_iterator:
            cpair[T, U]& operator*()
            iterator operator++()
            bint operator==(reverse_iterator)
            bint operator!=(reverse_iterator)
        cppclass const_iterator(iterator):
            pass
        cppclass const_reverse_iterator(reverse_iterator):
            pass

        std_unordered_map() except +
        std_unordered_map(std_unordered_map&) except +

        U& operator[](T&)
        iterator find(const T&)
        const_iterator const_find "find"(const T&)
        size_type count(const T&)
        size_type size()
        iterator begin()
        const_iterator const_begin "begin"()
        iterator end()
        const_iterator const_end "end"()
        reverse_iterator rbegin()
        const_reverse_iterator const_rbegin "rbegin"()
        reverse_iterator rend()
        const_reverse_iterator const_rend "rend"()
        void clear()
        bint empty()







cdef class std_unordered_map__Map__i32_string(thrift.py3.types.Map):
    cdef shared_ptr[std_unordered_map[cint32_t,string]] _cpp_obj
    @staticmethod
    cdef _fbthrift_create(shared_ptr[std_unordered_map[cint32_t,string]])
    @staticmethod
    cdef shared_ptr[std_unordered_map[cint32_t,string]] _make_instance(object items) except *

cdef class List__std_unordered_map__Map__i32_string(thrift.py3.types.List):
    cdef shared_ptr[vector[std_unordered_map[cint32_t,string]]] _cpp_obj
    @staticmethod
    cdef _fbthrift_create(shared_ptr[vector[std_unordered_map[cint32_t,string]]])
    @staticmethod
    cdef shared_ptr[vector[std_unordered_map[cint32_t,string]]] _make_instance(object items) except *


