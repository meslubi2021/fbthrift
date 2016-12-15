/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <cstddef>

#include <thrift/lib/cpp/Thrift.h>

#include "thrift/compiler/test/fixtures/constants/gen-cpp2/module_types.h"

namespace cpp2 {

struct _EmptyEnumEnumDataStorage {
  using type = EmptyEnum;
  static constexpr const std::size_t size = 0;
  static constexpr const std::array<EmptyEnum, 0> values = {{
  }};
  static constexpr const std::array<folly::StringPiece, 0> names = {{
  }};
};

} // cpp2
namespace apache { namespace thrift {

template <> struct TEnumDataStorage< ::cpp2::EmptyEnum> {
  using storage_type =  ::cpp2::_EmptyEnumEnumDataStorage;
};

}} // apache::thrift
namespace cpp2 {

struct _CityEnumDataStorage {
  using type = City;
  static constexpr const std::size_t size = 4;
  static constexpr const std::array<City, 4> values = {{
    City::NYC,
    City::MPK,
    City::SEA,
    City::LON,
  }};
  static constexpr const std::array<folly::StringPiece, 4> names = {{
    "NYC",
    "MPK",
    "SEA",
    "LON",
  }};
};

} // cpp2
namespace apache { namespace thrift {

template <> struct TEnumDataStorage< ::cpp2::City> {
  using storage_type =  ::cpp2::_CityEnumDataStorage;
};

}} // apache::thrift
namespace cpp2 {

struct _CompanyEnumDataStorage {
  using type = Company;
  static constexpr const std::size_t size = 4;
  static constexpr const std::array<Company, 4> values = {{
    Company::FACEBOOK,
    Company::WHATSAPP,
    Company::OCULUS,
    Company::INSTAGRAM,
  }};
  static constexpr const std::array<folly::StringPiece, 4> names = {{
    "FACEBOOK",
    "WHATSAPP",
    "OCULUS",
    "INSTAGRAM",
  }};
};

} // cpp2
namespace apache { namespace thrift {

template <> struct TEnumDataStorage< ::cpp2::Company> {
  using storage_type =  ::cpp2::_CompanyEnumDataStorage;
};

}} // apache::thrift

