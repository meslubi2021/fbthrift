#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/includes/src/matching_struct_names.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from libcpp.memory cimport shared_ptr

cimport matching_struct_names.cbindings as _fbthrift_cbindings


cdef shared_ptr[_fbthrift_cbindings.cMyStruct] MyStruct_convert_to_cpp(object inst) except*
cdef object MyStruct_from_cpp(const shared_ptr[_fbthrift_cbindings.cMyStruct]& c_struct)

cdef shared_ptr[_fbthrift_cbindings.cCombo] Combo_convert_to_cpp(object inst) except*
cdef object Combo_from_cpp(const shared_ptr[_fbthrift_cbindings.cCombo]& c_struct)

