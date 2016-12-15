/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <cstddef>

#include <thrift/lib/cpp/Thrift.h>

#include "thrift/compiler/test/fixtures/enum-strict/gen-cpp/module_types.h"


struct _EmptyEnumEnumDataStorage {
  using type = EmptyEnum;
  static constexpr const std::size_t size = 0;
  static constexpr const std::array<EmptyEnum, 0> values = {{
  }};
  static constexpr const std::array<folly::StringPiece, 0> names = {{
  }};
};

namespace apache { namespace thrift {
template <> struct TEnumDataStorage< ::EmptyEnum> {
  using storage_type =  ::_EmptyEnumEnumDataStorage;
};
}} // apache::thrift


struct _MyEnumEnumDataStorage {
  using type = MyEnum;
  static constexpr const std::size_t size = 2;
  static constexpr const std::array<MyEnum, 2> values = {{
    MyEnum::kMyFoo,
    MyEnum::kMyBar,
  }};
  static constexpr const std::array<folly::StringPiece, 2> names = {{
    "kMyFoo",
    "kMyBar",
  }};
};

namespace apache { namespace thrift {
template <> struct TEnumDataStorage< ::MyEnum> {
  using storage_type =  ::_MyEnumEnumDataStorage;
};
}} // apache::thrift

