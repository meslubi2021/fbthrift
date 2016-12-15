/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#include "thrift/compiler/test/fixtures/basic/gen-cpp/module_types.h"
#include "thrift/compiler/test/fixtures/basic/gen-cpp/module_data.h"

#include "thrift/compiler/test/fixtures/basic/gen-cpp/module_reflection.h"

#include <algorithm>
#include <string.h>



const typename apache::thrift::detail::TEnumMapFactory<MyEnum, int>::ValuesToNamesMapType _MyEnum_VALUES_TO_NAMES = apache::thrift::detail::TEnumMapFactory<MyEnum, int>::makeValuesToNamesMap();

const typename apache::thrift::detail::TEnumMapFactory<MyEnum, int>::NamesToValuesMapType _MyEnum_NAMES_TO_VALUES = apache::thrift::detail::TEnumMapFactory<MyEnum, int>::makeNamesToValuesMap();


namespace apache { namespace thrift {
template <>const std::size_t TEnumTraitsBase< ::MyEnum>::size = 2;
template <>const folly::Range<const  ::MyEnum*> TEnumTraitsBase< ::MyEnum>::values = folly::range( ::_MyEnumEnumDataStorage::values);
template <>const folly::Range<const folly::StringPiece*> TEnumTraitsBase< ::MyEnum>::names = folly::range( ::_MyEnumEnumDataStorage::names);

template<>
const char* TEnumTraitsBase< ::MyEnum>::findName( ::MyEnum value) {
return findName( ::_MyEnum_VALUES_TO_NAMES, value);
}

template<>
bool TEnumTraitsBase< ::MyEnum>::findValue(const char* name,  ::MyEnum* out) {
return findValue( ::_MyEnum_NAMES_TO_VALUES, name, out);
}
}} // apache::thrift



namespace apache { namespace thrift {
template<>
size_t Freezer< ::MyStruct, void>::extraSizeImpl(
    const Freezer< ::MyStruct, void>::ThawedType& src) {
  return 0
    + extraSize(src.MyIntField)
    + extraSize(src.MyStringField);
}

template<>
void Freezer< ::MyStruct, void>::freezeImpl(
    const Freezer< ::MyStruct, void>::ThawedType& src,
    Freezer< ::MyStruct, void>::FrozenType& dst,
    byte*& buffer) {
  freeze(src.MyIntField, dst.MyIntField, buffer);
  dst.__isset.MyIntField = src.__isset.MyIntField;
  freeze(src.MyStringField, dst.MyStringField, buffer);
  dst.__isset.MyStringField = src.__isset.MyStringField;
}

template<>
void Freezer< ::MyStruct, void>::thawImpl(
    const Freezer< ::MyStruct, void>::FrozenType& src,
    Freezer< ::MyStruct, void>::ThawedType& dst) {
  thaw(src.MyIntField, dst.MyIntField);
  dst.__isset.MyIntField = src.__isset.MyIntField;
  thaw(src.MyStringField, dst.MyStringField);
  dst.__isset.MyStringField = src.__isset.MyStringField;
}
}} // apache::thrift 


const uint64_t MyStruct::_reflection_id;
void MyStruct::_reflection_register(::apache::thrift::reflection::Schema& schema) {
   ::module_reflection_::reflectionInitializer_7958971832214294220(schema);
}

bool MyStruct::operator == (const MyStruct & rhs) const {
  if (!(this->MyIntField == rhs.MyIntField))
    return false;
  if (!(this->MyStringField == rhs.MyStringField))
    return false;
  return true;
}

uint32_t MyStruct::read(apache::thrift::protocol::TProtocol* iprot) {

  uint32_t xfer = 0;
  std::string fname;
  apache::thrift::protocol::TType ftype;
  int16_t fid;

  ::apache::thrift::reflection::Schema * schema = iprot->getSchema();
  if (schema != nullptr) {
     ::module_reflection_::reflectionInitializer_7958971832214294220(*schema);
    iprot->setNextStructType(MyStruct::_reflection_id);
  }
  xfer += iprot->readStructBegin(fname);

  using apache::thrift::protocol::TProtocolException;



  while (true)
  {
    xfer += iprot->readFieldBegin(fname, ftype, fid);
    if (ftype == apache::thrift::protocol::T_STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
        if (ftype == apache::thrift::protocol::T_I64) {
          xfer += iprot->readI64(this->MyIntField);
          this->__isset.MyIntField = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 2:
        if (ftype == apache::thrift::protocol::T_STRING) {
          xfer += iprot->readString(this->MyStringField);
          this->__isset.MyStringField = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      default:
        xfer += iprot->skip(ftype);
        break;
    }
    xfer += iprot->readFieldEnd();
  }

  xfer += iprot->readStructEnd();

  return xfer;
}

void MyStruct::__clear() {
  MyIntField = 0;
  MyStringField = "";
  __isset.__clear();
}
uint32_t MyStruct::write(apache::thrift::protocol::TProtocol* oprot) const {
  uint32_t xfer = 0;
  xfer += oprot->writeStructBegin("MyStruct");
  xfer += oprot->writeFieldBegin("MyIntField", apache::thrift::protocol::T_I64, 1);
  xfer += oprot->writeI64(this->MyIntField);
  xfer += oprot->writeFieldEnd();
  xfer += oprot->writeFieldBegin("MyStringField", apache::thrift::protocol::T_STRING, 2);
  xfer += oprot->writeString(this->MyStringField);
  xfer += oprot->writeFieldEnd();
  xfer += oprot->writeFieldStop();
  xfer += oprot->writeStructEnd();
  return xfer;
}

void swap(MyStruct &a, MyStruct &b) {
  using ::std::swap;
  (void)a;
  (void)b;
  swap(a.MyIntField, b.MyIntField);
  swap(a.MyStringField, b.MyStringField);
  swap(a.__isset, b.__isset);
}

void merge(const MyStruct& from, MyStruct& to) {
  using apache::thrift::merge;
  merge(from.MyIntField, to.MyIntField);
  to.__isset.MyIntField = to.__isset.MyIntField || from.__isset.MyIntField;
  merge(from.MyStringField, to.MyStringField);
  to.__isset.MyStringField = to.__isset.MyStringField || from.__isset.MyStringField;
}

void merge(MyStruct&& from, MyStruct& to) {
  using apache::thrift::merge;
  merge(std::move(from.MyIntField), to.MyIntField);
  to.__isset.MyIntField = to.__isset.MyIntField || from.__isset.MyIntField;
  merge(std::move(from.MyStringField), to.MyStringField);
  to.__isset.MyStringField = to.__isset.MyStringField || from.__isset.MyStringField;
}


