
#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/req-opt/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

cimport module.types as _fbthrift_ctypes


cdef shared_ptr[_fbthrift_cbindings.cFoo] Foo_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.Foo?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object Foo_from_cpp(const shared_ptr[_fbthrift_cbindings.cFoo]& c_struct):
    return _fbthrift_ctypes.Foo._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
