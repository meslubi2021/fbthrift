
#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/optionals/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

cimport module.types as _fbthrift_ctypes


cdef shared_ptr[_fbthrift_cbindings.cColor] Color_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.Color?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object Color_from_cpp(const shared_ptr[_fbthrift_cbindings.cColor]& c_struct):
    return _fbthrift_ctypes.Color._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cVehicle] Vehicle_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.Vehicle?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object Vehicle_from_cpp(const shared_ptr[_fbthrift_cbindings.cVehicle]& c_struct):
    return _fbthrift_ctypes.Vehicle._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
cdef shared_ptr[_fbthrift_cbindings.cPerson] Person_convert_to_cpp(object inst) except*:
    return (<_fbthrift_ctypes.Person?>inst)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE


cdef object Person_from_cpp(const shared_ptr[_fbthrift_cbindings.cPerson]& c_struct):
    return _fbthrift_ctypes.Person._create_FBTHRIFT_ONLY_DO_NOT_USE(c_struct)
