/**
 * Autogenerated by Thrift for thrift/compiler/test/fixtures/doctext/src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated @nocommit
 */
#include "thrift/compiler/test/fixtures/doctext/gen-cpp2/module_types.h"
#include "thrift/compiler/test/fixtures/doctext/gen-cpp2/module_types.tcc"

#include <thrift/lib/cpp2/gen/module_types_cpp.h>

#include "thrift/compiler/test/fixtures/doctext/gen-cpp2/module_data.h"


namespace apache { namespace thrift {

folly::Range<::cpp2::B const*> const TEnumTraits<::cpp2::B>::values = folly::range(TEnumDataStorage<::cpp2::B>::values);
folly::Range<folly::StringPiece const*> const TEnumTraits<::cpp2::B>::names = folly::range(TEnumDataStorage<::cpp2::B>::names);

bool TEnumTraits<::cpp2::B>::findName(type value, folly::StringPiece* out) noexcept {
  return ::apache::thrift::detail::st::enum_find_name(value, out);
}

bool TEnumTraits<::cpp2::B>::findValue(folly::StringPiece name, type* out) noexcept {
  return ::apache::thrift::detail::st::enum_find_value(name, out);
}

}} // apache::thrift


namespace apache {
namespace thrift {
namespace detail {

void TccStructTraits<::cpp2::A>::translateFieldName(
    folly::StringPiece _fname,
    int16_t& fid,
    apache::thrift::protocol::TType& _ftype) noexcept {
  using data = apache::thrift::TStructDataStorage<::cpp2::A>;
  static const st::translate_field_name_table table{
      data::fields_size,
      data::fields_names.data(),
      data::fields_ids.data(),
      data::fields_types.data()};
  st::translate_field_name(_fname, fid, _ftype, table);
}

} // namespace detail
} // namespace thrift
} // namespace apache

namespace cpp2 {

const folly::StringPiece A::__fbthrift_get_field_name(::apache::thrift::FieldOrdinal ord) {
  if (ord == ::apache::thrift::FieldOrdinal{0}) { return {}; }
  return apache::thrift::TStructDataStorage<A>::fields_names[folly::to_underlying(ord) - 1];
}
const folly::StringPiece A::__fbthrift_get_class_name() {
  return apache::thrift::TStructDataStorage<A>::name;
}


A::A(apache::thrift::FragileConstructor, ::std::int32_t useless_field__arg) :
    __fbthrift_field_useless_field(std::move(useless_field__arg)) {
  __isset.set(folly::index_constant<0>(), true);
}


void A::__fbthrift_clear() {
  // clear all fields
  this->__fbthrift_field_useless_field = ::std::int32_t();
  __isset = {};
}

void A::__fbthrift_clear_terse_fields() {
}

bool A::__fbthrift_is_empty() const {
  return false;
}

bool A::operator==(FOLLY_MAYBE_UNUSED const A& rhs) const {
  return ::apache::thrift::op::detail::StructEquality{}(*this, rhs);
}

bool A::operator<(FOLLY_MAYBE_UNUSED const A& rhs) const {
  return ::apache::thrift::op::detail::StructLessThan{}(*this, rhs);
}


void swap(FOLLY_MAYBE_UNUSED A& a, FOLLY_MAYBE_UNUSED A& b) {
  using ::std::swap;
  swap(a.__fbthrift_field_useless_field, b.__fbthrift_field_useless_field);
  swap(a.__isset, b.__isset);
}

template void A::readNoXfer<>(apache::thrift::BinaryProtocolReader*);
template uint32_t A::write<>(apache::thrift::BinaryProtocolWriter*) const;
template uint32_t A::serializedSize<>(apache::thrift::BinaryProtocolWriter const*) const;
template uint32_t A::serializedSizeZC<>(apache::thrift::BinaryProtocolWriter const*) const;
template void A::readNoXfer<>(apache::thrift::CompactProtocolReader*);
template uint32_t A::write<>(apache::thrift::CompactProtocolWriter*) const;
template uint32_t A::serializedSize<>(apache::thrift::CompactProtocolWriter const*) const;
template uint32_t A::serializedSizeZC<>(apache::thrift::CompactProtocolWriter const*) const;


} // cpp2

namespace apache {
namespace thrift {
namespace detail {

void TccStructTraits<::cpp2::U>::translateFieldName(
    folly::StringPiece _fname,
    int16_t& fid,
    apache::thrift::protocol::TType& _ftype) noexcept {
  using data = apache::thrift::TStructDataStorage<::cpp2::U>;
  static const st::translate_field_name_table table{
      data::fields_size,
      data::fields_names.data(),
      data::fields_ids.data(),
      data::fields_types.data()};
  st::translate_field_name(_fname, fid, _ftype, table);
}

} // namespace detail
} // namespace thrift
} // namespace apache

namespace apache { namespace thrift {

folly::Range<::cpp2::U::Type const*> const TEnumTraits<::cpp2::U::Type>::values = folly::range(TEnumDataStorage<::cpp2::U::Type>::values);
folly::Range<folly::StringPiece const*> const TEnumTraits<::cpp2::U::Type>::names = folly::range(TEnumDataStorage<::cpp2::U::Type>::names);

bool TEnumTraits<::cpp2::U::Type>::findName(type value, folly::StringPiece* out) noexcept {
  return ::apache::thrift::detail::st::enum_find_name(value, out);
}

bool TEnumTraits<::cpp2::U::Type>::findValue(folly::StringPiece name, type* out) noexcept {
  return ::apache::thrift::detail::st::enum_find_value(name, out);
}
}} // apache::thrift
namespace cpp2 {

const folly::StringPiece U::__fbthrift_get_field_name(::apache::thrift::FieldOrdinal ord) {
  if (ord == ::apache::thrift::FieldOrdinal{0}) { return {}; }
  return apache::thrift::TStructDataStorage<U>::fields_names[folly::to_underlying(ord) - 1];
}
const folly::StringPiece U::__fbthrift_get_class_name() {
  return apache::thrift::TStructDataStorage<U>::name;
}

void U::__fbthrift_destruct() {
  switch(getType()) {
    case Type::__EMPTY__:
      break;
    case Type::i:
      ::std::destroy_at(::std::addressof(value_.i));
      break;
    case Type::s:
      ::std::destroy_at(::std::addressof(value_.s));
      break;
    default:
      assert(false);
      break;
  }
}

void U::__fbthrift_clear() {
  __fbthrift_destruct();
  type_ = folly::to_underlying(Type::__EMPTY__);
}

  U::~U() {
    __fbthrift_destruct();
  }

bool U::__fbthrift_is_empty() const {
  return getType() == Type::__EMPTY__;
}
  U::U(const U& rhs)
      : type_(folly::to_underlying(Type::__EMPTY__)) {
    switch (rhs.getType()) {
      case Type::__EMPTY__:
        return;
      case Type::i:
        set_i(rhs.value_.i);
        break;
      case Type::s:
        set_s(rhs.value_.s);
        break;
      default:
        assert(false);
    }
  }

    U&U::operator=(const U& rhs) {
    if (this == &rhs) { return *this; }
    switch (rhs.getType()) {
      case Type::__EMPTY__:
        __fbthrift_clear();
        return *this;
      case Type::i:
        set_i(rhs.value_.i);
        break;
      case Type::s:
        set_s(rhs.value_.s);
        break;
      default:
        __fbthrift_clear();
        assert(false);
    }
    return *this;
  }


bool U::operator==(const U& rhs) const {
  return ::apache::thrift::op::detail::UnionEquality{}(*this, rhs);
}

bool U::operator<(FOLLY_MAYBE_UNUSED const U& rhs) const {
  return ::apache::thrift::op::detail::UnionLessThan{}(*this, rhs);
}

void swap(U& a, U& b) {
  U temp(std::move(a));
  a = std::move(b);
  b = std::move(temp);
}

template void U::readNoXfer<>(apache::thrift::BinaryProtocolReader*);
template uint32_t U::write<>(apache::thrift::BinaryProtocolWriter*) const;
template uint32_t U::serializedSize<>(apache::thrift::BinaryProtocolWriter const*) const;
template uint32_t U::serializedSizeZC<>(apache::thrift::BinaryProtocolWriter const*) const;
template void U::readNoXfer<>(apache::thrift::CompactProtocolReader*);
template uint32_t U::write<>(apache::thrift::CompactProtocolWriter*) const;
template uint32_t U::serializedSize<>(apache::thrift::CompactProtocolWriter const*) const;
template uint32_t U::serializedSizeZC<>(apache::thrift::CompactProtocolWriter const*) const;


} // cpp2

namespace apache {
namespace thrift {
namespace detail {

void TccStructTraits<::cpp2::Bang>::translateFieldName(
    folly::StringPiece _fname,
    int16_t& fid,
    apache::thrift::protocol::TType& _ftype) noexcept {
  using data = apache::thrift::TStructDataStorage<::cpp2::Bang>;
  static const st::translate_field_name_table table{
      data::fields_size,
      data::fields_names.data(),
      data::fields_ids.data(),
      data::fields_types.data()};
  st::translate_field_name(_fname, fid, _ftype, table);
}

} // namespace detail
} // namespace thrift
} // namespace apache

namespace cpp2 {

const folly::StringPiece Bang::__fbthrift_get_field_name(::apache::thrift::FieldOrdinal ord) {
  if (ord == ::apache::thrift::FieldOrdinal{0}) { return {}; }
  return apache::thrift::TStructDataStorage<Bang>::fields_names[folly::to_underlying(ord) - 1];
}
const folly::StringPiece Bang::__fbthrift_get_class_name() {
  return apache::thrift::TStructDataStorage<Bang>::name;
}

Bang::Bang(const Bang&) = default;
Bang& Bang::operator=(const Bang&) = default;
Bang::Bang() {
}


Bang::~Bang() {}

Bang::Bang(FOLLY_MAYBE_UNUSED Bang&& other) noexcept :
    __fbthrift_field_message(std::move(other.__fbthrift_field_message)),
    __isset(other.__isset) {
}

Bang& Bang::operator=(FOLLY_MAYBE_UNUSED Bang&& other) noexcept {
    this->__fbthrift_field_message = std::move(other.__fbthrift_field_message);
    __isset = other.__isset;
    return *this;
}


Bang::Bang(apache::thrift::FragileConstructor, ::std::string message__arg) :
    __fbthrift_field_message(std::move(message__arg)) {
  __isset.set(folly::index_constant<0>(), true);
}


void Bang::__fbthrift_clear() {
  // clear all fields
  this->__fbthrift_field_message = apache::thrift::StringTraits<std::string>::fromStringLiteral("");
  __isset = {};
}

void Bang::__fbthrift_clear_terse_fields() {
}

bool Bang::__fbthrift_is_empty() const {
  return false;
}

bool Bang::operator==(FOLLY_MAYBE_UNUSED const Bang& rhs) const {
  return ::apache::thrift::op::detail::StructEquality{}(*this, rhs);
}

bool Bang::operator<(FOLLY_MAYBE_UNUSED const Bang& rhs) const {
  return ::apache::thrift::op::detail::StructLessThan{}(*this, rhs);
}


void swap(FOLLY_MAYBE_UNUSED Bang& a, FOLLY_MAYBE_UNUSED Bang& b) {
  using ::std::swap;
  swap(a.__fbthrift_field_message, b.__fbthrift_field_message);
  swap(a.__isset, b.__isset);
}

template void Bang::readNoXfer<>(apache::thrift::BinaryProtocolReader*);
template uint32_t Bang::write<>(apache::thrift::BinaryProtocolWriter*) const;
template uint32_t Bang::serializedSize<>(apache::thrift::BinaryProtocolWriter const*) const;
template uint32_t Bang::serializedSizeZC<>(apache::thrift::BinaryProtocolWriter const*) const;
template void Bang::readNoXfer<>(apache::thrift::CompactProtocolReader*);
template uint32_t Bang::write<>(apache::thrift::CompactProtocolWriter*) const;
template uint32_t Bang::serializedSize<>(apache::thrift::CompactProtocolWriter const*) const;
template uint32_t Bang::serializedSizeZC<>(apache::thrift::CompactProtocolWriter const*) const;


} // cpp2

namespace cpp2 { namespace {
FOLLY_MAYBE_UNUSED FOLLY_ERASE void validateAdapters() {
}
}} // cpp2
namespace apache::thrift::detail::annotation {
}
