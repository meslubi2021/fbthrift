/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#include "thrift/annotation/gen-py3/java/metadata.h"

namespace facebook {
namespace thrift {
namespace annotation {
namespace java {
::apache::thrift::metadata::ThriftMetadata java_getThriftModuleMetadata() {
  ::apache::thrift::metadata::ThriftServiceMetadataResponse response;
  ::apache::thrift::metadata::ThriftMetadata& metadata = *response.metadata_ref();
  ::apache::thrift::detail::md::StructMetadata<Mutable>::gen(metadata);
  ::apache::thrift::detail::md::StructMetadata<Annotation>::gen(metadata);
  ::apache::thrift::detail::md::StructMetadata<BinaryString>::gen(metadata);
  ::apache::thrift::detail::md::StructMetadata<Adapter>::gen(metadata);
  ::apache::thrift::detail::md::StructMetadata<Wrapper>::gen(metadata);
  ::apache::thrift::detail::md::StructMetadata<Recursive>::gen(metadata);
  ::apache::thrift::detail::md::StructMetadata<FieldUseUnmangledName>::gen(metadata);
  return metadata;
}
} // namespace facebook
} // namespace thrift
} // namespace annotation
} // namespace java
