#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/complex-union/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from libcpp.memory cimport shared_ptr

cimport module.cbindings as _fbthrift_cbindings


cdef shared_ptr[_fbthrift_cbindings.cComplexUnion] ComplexUnion_convert_to_cpp(object inst) except*
cdef object ComplexUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cComplexUnion]& c_struct)

cdef shared_ptr[_fbthrift_cbindings.cListUnion] ListUnion_convert_to_cpp(object inst) except*
cdef object ListUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cListUnion]& c_struct)

cdef shared_ptr[_fbthrift_cbindings.cDataUnion] DataUnion_convert_to_cpp(object inst) except*
cdef object DataUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cDataUnion]& c_struct)

cdef shared_ptr[_fbthrift_cbindings.cVal] Val_convert_to_cpp(object inst) except*
cdef object Val_from_cpp(const shared_ptr[_fbthrift_cbindings.cVal]& c_struct)

cdef shared_ptr[_fbthrift_cbindings.cValUnion] ValUnion_convert_to_cpp(object inst) except*
cdef object ValUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cValUnion]& c_struct)

cdef shared_ptr[_fbthrift_cbindings.cVirtualComplexUnion] VirtualComplexUnion_convert_to_cpp(object inst) except*
cdef object VirtualComplexUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cVirtualComplexUnion]& c_struct)

cdef shared_ptr[_fbthrift_cbindings.cNonCopyableStruct] NonCopyableStruct_convert_to_cpp(object inst) except*
cdef object NonCopyableStruct_from_cpp(const shared_ptr[_fbthrift_cbindings.cNonCopyableStruct]& c_struct)

cdef shared_ptr[_fbthrift_cbindings.cNonCopyableUnion] NonCopyableUnion_convert_to_cpp(object inst) except*
cdef object NonCopyableUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cNonCopyableUnion]& c_struct)

