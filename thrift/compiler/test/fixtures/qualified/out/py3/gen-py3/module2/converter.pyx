
#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/qualified/src/module2.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

cimport module2.types as _fbthrift_ctypes


cdef shared_ptr[_fbthrift_cbindings.cStruct] Struct_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.Struct?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object Struct_from_cpp(const shared_ptr[_fbthrift_cbindings.cStruct]& c_struct):
    return _fbthrift_ctypes.Struct._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cBigStruct] BigStruct_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.BigStruct?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object BigStruct_from_cpp(const shared_ptr[_fbthrift_cbindings.cBigStruct]& c_struct):
    return _fbthrift_ctypes.BigStruct._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
