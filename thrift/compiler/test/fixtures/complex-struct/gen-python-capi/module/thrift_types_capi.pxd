
#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from cpython.ref cimport PyObject
from libc.stdint cimport int64_t
from libcpp.memory cimport unique_ptr as __unique_ptr

from folly.iobuf cimport cIOBuf as __cIOBuf


cdef api int can_extract__module__MyStructFloatFieldThrowExp(object) except -1


cdef api object init__module__MyStructFloatFieldThrowExp(object data)

cdef api int can_extract__module__MyStructMapFloatThrowExp(object) except -1


cdef api object init__module__MyStructMapFloatThrowExp(object data)

cdef api int can_extract__module__MyStruct(object) except -1


cdef api object init__module__MyStruct(object data)

cdef api int can_extract__module__SimpleStruct(object) except -1


cdef api object init__module__SimpleStruct(object data)

cdef api int can_extract__module__defaultStruct(object) except -1


cdef api object init__module__defaultStruct(object data)

cdef api int can_extract__module__MyStructTypeDef(object) except -1


cdef api object init__module__MyStructTypeDef(object data)

cdef api int can_extract__module__MyDataItem(object) except -1


cdef api object init__module__MyDataItem(object data)

cdef api int can_extract__module__MyUnion(object) except -1

cdef api __cIOBuf* extract__module__MyUnion(object) except NULL

cdef api object construct__module__MyUnion(__unique_ptr[__cIOBuf])

cdef api object init__module__MyUnion(object data)

cdef api int can_extract__module__MyUnionFloatFieldThrowExp(object) except -1

cdef api __cIOBuf* extract__module__MyUnionFloatFieldThrowExp(object) except NULL

cdef api object construct__module__MyUnionFloatFieldThrowExp(__unique_ptr[__cIOBuf])

cdef api object init__module__MyUnionFloatFieldThrowExp(object data)

cdef api int can_extract__module__ComplexNestedStruct(object) except -1


cdef api object init__module__ComplexNestedStruct(object data)

cdef api int can_extract__module__TypeRemapped(object) except -1


cdef api object init__module__TypeRemapped(object data)

cdef api int can_extract__module__emptyXcep(object) except -1


cdef api object init__module__emptyXcep(object data)

cdef api int can_extract__module__reqXcep(object) except -1


cdef api object init__module__reqXcep(object data)

cdef api int can_extract__module__optXcep(object) except -1


cdef api object init__module__optXcep(object data)

cdef api int can_extract__module__complexException(object) except -1


cdef api object init__module__complexException(object data)

cdef api int can_extract__module__MyEnum(object) except -1

cdef api object construct__module__MyEnum(int64_t)

