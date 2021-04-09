/**
 * Autogenerated by Thrift for src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include "thrift/compiler/test/fixtures/tablebased/gen-cpp2/module_types.h"

#include <thrift/lib/cpp2/gen/module_types_tcc.h>

namespace test { namespace fixtures { namespace tablebased {

}}} // test::fixtures::tablebased
namespace std {

} // std


namespace test { namespace fixtures { namespace tablebased {
extern const ::apache::thrift::detail::StructInfoN<5> __fbthrift_struct_info_TrivialTypesStruct;

template <class Protocol_>
void TrivialTypesStruct::readNoXfer(Protocol_* iprot) {
  ::apache::thrift::detail::read(
    iprot,
    ::apache::thrift::detail::toStructInfo(
      ::test::fixtures::tablebased::__fbthrift_struct_info_TrivialTypesStruct
    ),
    this);
}

template <class Protocol_>
uint32_t TrivialTypesStruct::serializedSize(Protocol_ const* prot_) const {
  uint32_t xfer = 0;
  xfer += prot_->serializedStructSize("TrivialTypesStruct");
  if (this->fieldA_ref().has_value()) {
    xfer += prot_->serializedFieldSize("fieldA", apache::thrift::protocol::T_I32, 1);
    xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::integral, ::std::int32_t>::serializedSize<false>(*prot_, this->fieldA);
  }
  if (this->fieldB_ref().has_value()) {
    xfer += prot_->serializedFieldSize("fieldB", apache::thrift::protocol::T_STRING, 2);
    xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::string, ::std::string>::serializedSize<false>(*prot_, this->fieldB);
  }
  if (this->fieldC_ref().has_value()) {
    xfer += prot_->serializedFieldSize("fieldC", apache::thrift::protocol::T_STRING, 3);
    xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::binary, ::std::string>::serializedSize<false>(*prot_, this->fieldC);
  }
  if (this->fieldD_ref().has_value()) {
    xfer += prot_->serializedFieldSize("fieldD", apache::thrift::protocol::T_STRING, 4);
    xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::binary, ::test::fixtures::tablebased::IOBufPtr>::serializedSize<false>(*prot_, this->fieldD);
  }
  xfer += prot_->serializedFieldSize("fieldE", apache::thrift::protocol::T_I32, 5);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::enumeration, ::test::fixtures::tablebased::ExampleEnum>::serializedSize<false>(*prot_, this->fieldE);
  xfer += prot_->serializedSizeStop();
  return xfer;
}

template <class Protocol_>
uint32_t TrivialTypesStruct::serializedSizeZC(Protocol_ const* prot_) const {
  uint32_t xfer = 0;
  xfer += prot_->serializedStructSize("TrivialTypesStruct");
  if (this->fieldA_ref().has_value()) {
    xfer += prot_->serializedFieldSize("fieldA", apache::thrift::protocol::T_I32, 1);
    xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::integral, ::std::int32_t>::serializedSize<false>(*prot_, this->fieldA);
  }
  if (this->fieldB_ref().has_value()) {
    xfer += prot_->serializedFieldSize("fieldB", apache::thrift::protocol::T_STRING, 2);
    xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::string, ::std::string>::serializedSize<false>(*prot_, this->fieldB);
  }
  if (this->fieldC_ref().has_value()) {
    xfer += prot_->serializedFieldSize("fieldC", apache::thrift::protocol::T_STRING, 3);
    xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::binary, ::std::string>::serializedSize<true>(*prot_, this->fieldC);
  }
  if (this->fieldD_ref().has_value()) {
    xfer += prot_->serializedFieldSize("fieldD", apache::thrift::protocol::T_STRING, 4);
    xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::binary, ::test::fixtures::tablebased::IOBufPtr>::serializedSize<true>(*prot_, this->fieldD);
  }
  xfer += prot_->serializedFieldSize("fieldE", apache::thrift::protocol::T_I32, 5);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::enumeration, ::test::fixtures::tablebased::ExampleEnum>::serializedSize<false>(*prot_, this->fieldE);
  xfer += prot_->serializedSizeStop();
  return xfer;
}

template <class Protocol_>
uint32_t TrivialTypesStruct::write(Protocol_* iprot) const {
  return ::apache::thrift::detail::write(
    iprot,
    ::apache::thrift::detail::toStructInfo(
      ::test::fixtures::tablebased::__fbthrift_struct_info_TrivialTypesStruct
    ),
    this);
}

extern template void TrivialTypesStruct::readNoXfer<>(apache::thrift::BinaryProtocolReader*);
extern template uint32_t TrivialTypesStruct::write<>(apache::thrift::BinaryProtocolWriter*) const;
extern template uint32_t TrivialTypesStruct::serializedSize<>(apache::thrift::BinaryProtocolWriter const*) const;
extern template uint32_t TrivialTypesStruct::serializedSizeZC<>(apache::thrift::BinaryProtocolWriter const*) const;
extern template void TrivialTypesStruct::readNoXfer<>(apache::thrift::CompactProtocolReader*);
extern template uint32_t TrivialTypesStruct::write<>(apache::thrift::CompactProtocolWriter*) const;
extern template uint32_t TrivialTypesStruct::serializedSize<>(apache::thrift::CompactProtocolWriter const*) const;
extern template uint32_t TrivialTypesStruct::serializedSizeZC<>(apache::thrift::CompactProtocolWriter const*) const;
extern template void TrivialTypesStruct::readNoXfer<>(apache::thrift::SimpleJSONProtocolReader*);
extern template uint32_t TrivialTypesStruct::write<>(apache::thrift::SimpleJSONProtocolWriter*) const;
extern template uint32_t TrivialTypesStruct::serializedSize<>(apache::thrift::SimpleJSONProtocolWriter const*) const;
extern template uint32_t TrivialTypesStruct::serializedSizeZC<>(apache::thrift::SimpleJSONProtocolWriter const*) const;

}}} // test::fixtures::tablebased
namespace test { namespace fixtures { namespace tablebased {
extern const ::apache::thrift::detail::StructInfoN<8> __fbthrift_struct_info_ContainerStruct;

template <class Protocol_>
void ContainerStruct::readNoXfer(Protocol_* iprot) {
  ::apache::thrift::detail::read(
    iprot,
    ::apache::thrift::detail::toStructInfo(
      ::test::fixtures::tablebased::__fbthrift_struct_info_ContainerStruct
    ),
    this);
}

template <class Protocol_>
uint32_t ContainerStruct::serializedSize(Protocol_ const* prot_) const {
  uint32_t xfer = 0;
  xfer += prot_->serializedStructSize("ContainerStruct");
  xfer += prot_->serializedFieldSize("fieldA", apache::thrift::protocol::T_LIST, 12);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, ::std::vector<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldA);
  xfer += prot_->serializedFieldSize("fieldB", apache::thrift::protocol::T_LIST, 2);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, std::list<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldB);
  xfer += prot_->serializedFieldSize("fieldC", apache::thrift::protocol::T_LIST, 3);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, std::deque<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldC);
  xfer += prot_->serializedFieldSize("fieldD", apache::thrift::protocol::T_LIST, 4);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, folly::fbvector<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldD);
  xfer += prot_->serializedFieldSize("fieldE", apache::thrift::protocol::T_LIST, 5);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, folly::small_vector<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldE);
  xfer += prot_->serializedFieldSize("fieldF", apache::thrift::protocol::T_SET, 6);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::set<::apache::thrift::type_class::integral>, folly::sorted_vector_set<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldF);
  xfer += prot_->serializedFieldSize("fieldG", apache::thrift::protocol::T_MAP, 7);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::map<::apache::thrift::type_class::integral, ::apache::thrift::type_class::string>, folly::sorted_vector_map<::std::int32_t, ::std::string>>::serializedSize<false>(*prot_, this->fieldG);
  xfer += prot_->serializedFieldSize("fieldH", apache::thrift::protocol::T_LIST, 8);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::structure>, ::std::vector<::test::fixtures::tablebased::TrivialTypesStruct>>::serializedSize<false>(*prot_, this->fieldH);
  xfer += prot_->serializedSizeStop();
  return xfer;
}

template <class Protocol_>
uint32_t ContainerStruct::serializedSizeZC(Protocol_ const* prot_) const {
  uint32_t xfer = 0;
  xfer += prot_->serializedStructSize("ContainerStruct");
  xfer += prot_->serializedFieldSize("fieldA", apache::thrift::protocol::T_LIST, 12);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, ::std::vector<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldA);
  xfer += prot_->serializedFieldSize("fieldB", apache::thrift::protocol::T_LIST, 2);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, std::list<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldB);
  xfer += prot_->serializedFieldSize("fieldC", apache::thrift::protocol::T_LIST, 3);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, std::deque<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldC);
  xfer += prot_->serializedFieldSize("fieldD", apache::thrift::protocol::T_LIST, 4);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, folly::fbvector<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldD);
  xfer += prot_->serializedFieldSize("fieldE", apache::thrift::protocol::T_LIST, 5);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::integral>, folly::small_vector<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldE);
  xfer += prot_->serializedFieldSize("fieldF", apache::thrift::protocol::T_SET, 6);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::set<::apache::thrift::type_class::integral>, folly::sorted_vector_set<::std::int32_t>>::serializedSize<false>(*prot_, this->fieldF);
  xfer += prot_->serializedFieldSize("fieldG", apache::thrift::protocol::T_MAP, 7);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::map<::apache::thrift::type_class::integral, ::apache::thrift::type_class::string>, folly::sorted_vector_map<::std::int32_t, ::std::string>>::serializedSize<false>(*prot_, this->fieldG);
  xfer += prot_->serializedFieldSize("fieldH", apache::thrift::protocol::T_LIST, 8);
  xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::list<::apache::thrift::type_class::structure>, ::std::vector<::test::fixtures::tablebased::TrivialTypesStruct>>::serializedSize<false>(*prot_, this->fieldH);
  xfer += prot_->serializedSizeStop();
  return xfer;
}

template <class Protocol_>
uint32_t ContainerStruct::write(Protocol_* iprot) const {
  return ::apache::thrift::detail::write(
    iprot,
    ::apache::thrift::detail::toStructInfo(
      ::test::fixtures::tablebased::__fbthrift_struct_info_ContainerStruct
    ),
    this);
}

extern template void ContainerStruct::readNoXfer<>(apache::thrift::BinaryProtocolReader*);
extern template uint32_t ContainerStruct::write<>(apache::thrift::BinaryProtocolWriter*) const;
extern template uint32_t ContainerStruct::serializedSize<>(apache::thrift::BinaryProtocolWriter const*) const;
extern template uint32_t ContainerStruct::serializedSizeZC<>(apache::thrift::BinaryProtocolWriter const*) const;
extern template void ContainerStruct::readNoXfer<>(apache::thrift::CompactProtocolReader*);
extern template uint32_t ContainerStruct::write<>(apache::thrift::CompactProtocolWriter*) const;
extern template uint32_t ContainerStruct::serializedSize<>(apache::thrift::CompactProtocolWriter const*) const;
extern template uint32_t ContainerStruct::serializedSizeZC<>(apache::thrift::CompactProtocolWriter const*) const;
extern template void ContainerStruct::readNoXfer<>(apache::thrift::SimpleJSONProtocolReader*);
extern template uint32_t ContainerStruct::write<>(apache::thrift::SimpleJSONProtocolWriter*) const;
extern template uint32_t ContainerStruct::serializedSize<>(apache::thrift::SimpleJSONProtocolWriter const*) const;
extern template uint32_t ContainerStruct::serializedSizeZC<>(apache::thrift::SimpleJSONProtocolWriter const*) const;

}}} // test::fixtures::tablebased
namespace test { namespace fixtures { namespace tablebased {
extern const ::apache::thrift::detail::StructInfoN<2> __fbthrift_struct_info_ExampleUnion;


template <class Protocol_>
void ExampleUnion::readNoXfer(Protocol_* iprot) {
  ::apache::thrift::detail::read(
    iprot,
    ::apache::thrift::detail::toStructInfo(
      ::test::fixtures::tablebased::__fbthrift_struct_info_ExampleUnion
    ),
    this);
}
template <class Protocol_>
uint32_t ExampleUnion::serializedSize(Protocol_ const* prot_) const {
  uint32_t xfer = 0;
  xfer += prot_->serializedStructSize("ExampleUnion");
  switch(this->getType()) {
    case ExampleUnion::Type::fieldA:
    {
      xfer += prot_->serializedFieldSize("fieldA", apache::thrift::protocol::T_STRUCT, 1);
      xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::structure, ::test::fixtures::tablebased::ContainerStruct>::serializedSize<false>(*prot_, this->value_.fieldA);
      break;
    }
    case ExampleUnion::Type::fieldB:
    {
      xfer += prot_->serializedFieldSize("fieldB", apache::thrift::protocol::T_STRUCT, 2);
      xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::structure, ::test::fixtures::tablebased::TrivialTypesStruct>::serializedSize<false>(*prot_, this->value_.fieldB);
      break;
    }
    case ExampleUnion::Type::__EMPTY__:;
  }
  xfer += prot_->serializedSizeStop();
  return xfer;
}

template <class Protocol_>
uint32_t ExampleUnion::serializedSizeZC(Protocol_ const* prot_) const {
  uint32_t xfer = 0;
  xfer += prot_->serializedStructSize("ExampleUnion");
  switch(this->getType()) {
    case ExampleUnion::Type::fieldA:
    {
      xfer += prot_->serializedFieldSize("fieldA", apache::thrift::protocol::T_STRUCT, 1);
      xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::structure, ::test::fixtures::tablebased::ContainerStruct>::serializedSize<true>(*prot_, this->value_.fieldA);
      break;
    }
    case ExampleUnion::Type::fieldB:
    {
      xfer += prot_->serializedFieldSize("fieldB", apache::thrift::protocol::T_STRUCT, 2);
      xfer += ::apache::thrift::detail::pm::protocol_methods<::apache::thrift::type_class::structure, ::test::fixtures::tablebased::TrivialTypesStruct>::serializedSize<true>(*prot_, this->value_.fieldB);
      break;
    }
    case ExampleUnion::Type::__EMPTY__:;
  }
  xfer += prot_->serializedSizeStop();
  return xfer;
}

template <class Protocol_>
uint32_t ExampleUnion::write(Protocol_* iprot) const {
  return ::apache::thrift::detail::write(
    iprot,
    ::apache::thrift::detail::toStructInfo(
      ::test::fixtures::tablebased::__fbthrift_struct_info_ExampleUnion
    ),
    this);
}

extern template void ExampleUnion::readNoXfer<>(apache::thrift::BinaryProtocolReader*);
extern template uint32_t ExampleUnion::write<>(apache::thrift::BinaryProtocolWriter*) const;
extern template uint32_t ExampleUnion::serializedSize<>(apache::thrift::BinaryProtocolWriter const*) const;
extern template uint32_t ExampleUnion::serializedSizeZC<>(apache::thrift::BinaryProtocolWriter const*) const;
extern template void ExampleUnion::readNoXfer<>(apache::thrift::CompactProtocolReader*);
extern template uint32_t ExampleUnion::write<>(apache::thrift::CompactProtocolWriter*) const;
extern template uint32_t ExampleUnion::serializedSize<>(apache::thrift::CompactProtocolWriter const*) const;
extern template uint32_t ExampleUnion::serializedSizeZC<>(apache::thrift::CompactProtocolWriter const*) const;
extern template void ExampleUnion::readNoXfer<>(apache::thrift::SimpleJSONProtocolReader*);
extern template uint32_t ExampleUnion::write<>(apache::thrift::SimpleJSONProtocolWriter*) const;
extern template uint32_t ExampleUnion::serializedSize<>(apache::thrift::SimpleJSONProtocolWriter const*) const;
extern template uint32_t ExampleUnion::serializedSizeZC<>(apache::thrift::SimpleJSONProtocolWriter const*) const;

}}} // test::fixtures::tablebased
