
#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/complex-union/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

cimport module.types as _fbthrift_ctypes


cdef shared_ptr[_fbthrift_cbindings.cComplexUnion] ComplexUnion_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.ComplexUnion?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object ComplexUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cComplexUnion]& c_struct):
    return _fbthrift_ctypes.ComplexUnion._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cListUnion] ListUnion_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.ListUnion?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object ListUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cListUnion]& c_struct):
    return _fbthrift_ctypes.ListUnion._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cDataUnion] DataUnion_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.DataUnion?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object DataUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cDataUnion]& c_struct):
    return _fbthrift_ctypes.DataUnion._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cVal] Val_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.Val?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object Val_from_cpp(const shared_ptr[_fbthrift_cbindings.cVal]& c_struct):
    return _fbthrift_ctypes.Val._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cValUnion] ValUnion_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.ValUnion?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object ValUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cValUnion]& c_struct):
    return _fbthrift_ctypes.ValUnion._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cVirtualComplexUnion] VirtualComplexUnion_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.VirtualComplexUnion?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object VirtualComplexUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cVirtualComplexUnion]& c_struct):
    return _fbthrift_ctypes.VirtualComplexUnion._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cNonCopyableStruct] NonCopyableStruct_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.NonCopyableStruct?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object NonCopyableStruct_from_cpp(const shared_ptr[_fbthrift_cbindings.cNonCopyableStruct]& c_struct):
    return _fbthrift_ctypes.NonCopyableStruct._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cNonCopyableUnion] NonCopyableUnion_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.NonCopyableUnion?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object NonCopyableUnion_from_cpp(const shared_ptr[_fbthrift_cbindings.cNonCopyableUnion]& c_struct):
    return _fbthrift_ctypes.NonCopyableUnion._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
