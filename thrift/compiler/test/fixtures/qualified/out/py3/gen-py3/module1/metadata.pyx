#
# Autogenerated by Thrift for module1.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from libcpp.memory cimport shared_ptr, make_shared
from libcpp.utility cimport move as cmove

from apache.thrift.metadata.cbindings cimport (
    cThriftMetadata,
)
from apache.thrift.metadata.types cimport (
    ThriftMetadata,
)

from module1.metadata cimport cGetThriftModuleMetadata

def getThriftModuleMetadata():
    cdef shared_ptr[cThriftMetadata] metadata
    metadata = make_shared[cThriftMetadata](cGetThriftModuleMetadata())
    return ThriftMetadata._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(metadata))
