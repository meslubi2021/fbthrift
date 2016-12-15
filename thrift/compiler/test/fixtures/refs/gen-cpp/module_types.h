/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <thrift/lib/cpp/Thrift.h>
#include <thrift/lib/cpp/TApplicationException.h>
#include <thrift/lib/cpp/protocol/TProtocol.h>
#include <thrift/lib/cpp/transport/TTransport.h>

namespace apache { namespace thrift { namespace reflection {
class Schema;
}}}




enum TypedEnum : short {
  VAL1 = 0,
  VAL2 = 1,
};

extern const typename apache::thrift::detail::TEnumMapFactory<TypedEnum, short>::ValuesToNamesMapType _TypedEnum_VALUES_TO_NAMES;

extern const typename apache::thrift::detail::TEnumMapFactory<TypedEnum, short>::NamesToValuesMapType _TypedEnum_NAMES_TO_VALUES;


namespace apache { namespace thrift {
template <> struct TEnumDataStorage< ::TypedEnum>;
template <> const std::size_t TEnumTraitsBase< ::TypedEnum>::size;
template <> const folly::Range<const  ::TypedEnum*> TEnumTraitsBase< ::TypedEnum>::values;
template <> const folly::Range<const folly::StringPiece*> TEnumTraitsBase< ::TypedEnum>::names;
}} // apache::thrift




namespace apache { namespace thrift {
template<>
struct TEnumTraits< ::TypedEnum> : public TEnumTraitsBase< ::TypedEnum>
{
inline static constexpr  ::TypedEnum min() {
return  ::TypedEnum::VAL1;
}
inline static constexpr  ::TypedEnum max() {
return  ::TypedEnum::VAL2;
}
};
}} // apache:thrift


class MyUnion;

class MyField;

class MyStruct;

class StructWithUnion;

class RecursiveStruct;

class StructWithContainers;

class StructWithSharedConst;

class MyUnion : public apache::thrift::TStructType<MyUnion> {
 public:
  enum class Type {
    __EMPTY__ = 0,
    anInteger = 1,
    aString = 2,
  };

  MyUnion() : type_(Type::__EMPTY__) {}
  template <typename T__ThriftWrappedArgument__Ctor>
  explicit MyUnion(
    ::apache::thrift::detail::argument_wrapper<1, T__ThriftWrappedArgument__Ctor> arg):
    type_(Type::__EMPTY__)
  {
    set_anInteger(arg.move());
  }
  template <typename T__ThriftWrappedArgument__Ctor>
  explicit MyUnion(
    ::apache::thrift::detail::argument_wrapper<2, T__ThriftWrappedArgument__Ctor> arg):
    type_(Type::__EMPTY__)
  {
    set_aString(arg.move());
  }
  MyUnion(const MyUnion& rhs) : type_(Type::__EMPTY__) {
    if (this == &rhs) { return; }
    if (rhs.type_ == Type::__EMPTY__) { return; }
    switch (rhs.type_) {
      case Type::anInteger: {
        set_anInteger(rhs.value_.anInteger);
        break;
      }
      case Type::aString: {
        set_aString(rhs.value_.aString);
        break;
      }
      default: assert(false);
    }
  }

  MyUnion& operator=(const MyUnion& rhs) {
    if (this == &rhs) { return *this; }
    __clear();
    if (rhs.type_ == Type::__EMPTY__) { return *this; }
    switch (rhs.type_) {
      case Type::anInteger: {
        set_anInteger(rhs.value_.anInteger);
        break;
      }
      case Type::aString: {
        set_aString(rhs.value_.aString);
        break;
      }
      default: assert(false);
    }
    return *this;
  }

  MyUnion(MyUnion&& rhs) : type_(Type::__EMPTY__) {
    if (this == &rhs) { return; }
    if (rhs.type_ == Type::__EMPTY__) { return; }
    switch (rhs.type_) {
      case Type::anInteger: {
        set_anInteger(std::move(rhs.value_.anInteger));
        break;
      }
      case Type::aString: {
        set_aString(std::move(rhs.value_.aString));
        break;
      }
      default: assert(false);
    }
    rhs.__clear();
  }

  MyUnion& operator=(MyUnion&& rhs) {
    if (this == &rhs) { return *this; }
    __clear();
    if (rhs.type_ == Type::__EMPTY__) { return *this; }
    switch (rhs.type_) {
      case Type::anInteger: {
        set_anInteger(std::move(rhs.value_.anInteger));
        break;
      }
      case Type::aString: {
        set_aString(std::move(rhs.value_.aString));
        break;
      }
      default: assert(false);
    }
    rhs.__clear();
    return *this;
  }


  void __clear() {
    if (type_ == Type::__EMPTY__) { return; }
    switch (type_) {
      case Type::anInteger: {
        
        break;
      }
      case Type::aString: {
        using namespace std; value_.aString.~string();
        break;
      }
      default: assert(false);
    }
    type_ = Type::__EMPTY__;
  }
  virtual ~MyUnion() throw() {
    __clear();
  }

  union storage_type {
    int32_t anInteger;
    std::string aString;
    
    storage_type() {}
    ~storage_type() {}
  };

  bool operator==(const MyUnion& rhs) const {
    if (type_ != rhs.type_) { return false; }
    switch (type_) {
      case Type::anInteger: {
        return value_.anInteger == rhs.value_.anInteger;

        break;
      }
      case Type::aString: {
        return value_.aString == rhs.value_.aString;

        break;
      }
      default: return true;
    }
  }

  bool operator!=(const MyUnion& rhs) const {
    return !(*this == rhs);
  }

  bool operator<(const MyUnion& rhs) const {
    if (type_ != rhs.type_) return type_ < rhs.type_;
    switch (type_) {
      case Type::anInteger: {
        return value_.anInteger < rhs.value_.anInteger;

        break;
      }
      case Type::aString: {
        return value_.aString < rhs.value_.aString;

        break;
      }
      default: return false;
    }
    return false;
  }

  template<typename... T>
  void set_anInteger(T&&... t) {
    __clear();
    type_ = Type::anInteger;
    new (&value_.anInteger) int32_t(std::forward<T>(t)...);
  }

  template<typename... T>
  void set_aString(T&&... t) {
    __clear();
    type_ = Type::aString;
    new (&value_.aString) std::string(std::forward<T>(t)...);
  }

  const int32_t& get_anInteger() const {
    assert(type_ == Type::anInteger);
    return value_.anInteger;
  }

  const std::string& get_aString() const {
    assert(type_ == Type::aString);
    return value_.aString;
  }

  int32_t& mutable_anInteger() {
    assert(type_ == Type::anInteger);
    return value_.anInteger;
  }

  std::string& mutable_aString() {
    assert(type_ == Type::aString);
    return value_.aString;
  }

  int32_t move_anInteger() {
    assert(type_ == Type::anInteger);
    return std::move(value_.anInteger);
  }

  std::string move_aString() {
    assert(type_ == Type::aString);
    return std::move(value_.aString);
  }

  Type getType() const { return type_; }

  uint32_t read(apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(apache::thrift::protocol::TProtocol* oprot) const;
 private:
  Type type_;
  storage_type value_;

};

void swap(MyField &a, MyField &b);

class MyField : public apache::thrift::TStructType<MyField> {
 public:

  static const uint64_t _reflection_id = 16778989117799402412U;
  static void _reflection_register(::apache::thrift::reflection::Schema&);
  MyField() : opt_value(0), value(0), req_value(0) {
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit MyField(
    ::apache::thrift::detail::argument_wrapper<1, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    MyField(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    opt_value = arg.move();
    __isset.opt_value = true;
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit MyField(
    ::apache::thrift::detail::argument_wrapper<2, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    MyField(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    value = arg.move();
    __isset.value = true;
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit MyField(
    ::apache::thrift::detail::argument_wrapper<3, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    MyField(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    req_value = arg.move();
  }

  MyField(const MyField&) = default;
  MyField& operator=(const MyField& src)= default;
  MyField(MyField&&) = default;
  MyField& operator=(MyField&&) = default;

  void __clear();

  virtual ~MyField() throw() {}

  int64_t opt_value;
  int64_t value;
  int64_t req_value;

  struct __isset {
    __isset() { __clear(); } 
    void __clear() {
      opt_value = false;
      value = false;
    }
    bool opt_value;
    bool value;
  } __isset;

  bool operator == (const MyField &) const;
  bool operator != (const MyField& rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const MyField & ) const;

  uint32_t read(apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(apache::thrift::protocol::TProtocol* oprot) const;

};

class MyField;
void merge(const MyField& from, MyField& to);
void merge(MyField&& from, MyField& to);
void swap(MyStruct &a, MyStruct &b);

class MyStruct : public apache::thrift::TStructType<MyStruct> {
 public:

  static const uint64_t _reflection_id = 7958971832214294220U;
  static void _reflection_register(::apache::thrift::reflection::Schema&);
  MyStruct() {
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit MyStruct(
    ::apache::thrift::detail::argument_wrapper<1, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    MyStruct(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    opt_ref = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit MyStruct(
    ::apache::thrift::detail::argument_wrapper<2, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    MyStruct(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    ref = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit MyStruct(
    ::apache::thrift::detail::argument_wrapper<3, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    MyStruct(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    req_ref = arg.move();
  }

  MyStruct(const MyStruct&);
  MyStruct& operator=(const MyStruct& src) {
    MyStruct tmp(src);
    swap(*this, tmp);
    return *this;
  }
  MyStruct(MyStruct&&) = default;
  MyStruct& operator=(MyStruct&&) = default;

  void __clear();

  virtual ~MyStruct() throw() {}

  std::unique_ptr<MyField> opt_ref;
  std::unique_ptr<MyField> ref;
  std::unique_ptr<MyField> req_ref;

  struct __isset {
    __isset() { __clear(); } 
    void __clear() {
    }
  } __isset;

  bool operator == (const MyStruct &) const;
  bool operator != (const MyStruct& rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const MyStruct & ) const;

  uint32_t read(apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(apache::thrift::protocol::TProtocol* oprot) const;

};

class MyStruct;
void merge(const MyStruct& from, MyStruct& to);
void merge(MyStruct&& from, MyStruct& to);
void swap(StructWithUnion &a, StructWithUnion &b);

class StructWithUnion : public apache::thrift::TStructType<StructWithUnion> {
 public:

  static const uint64_t _reflection_id = 11295191354176986988U;
  static void _reflection_register(::apache::thrift::reflection::Schema&);
  StructWithUnion() : aDouble(0) {
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithUnion(
    ::apache::thrift::detail::argument_wrapper<1, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithUnion(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    u = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithUnion(
    ::apache::thrift::detail::argument_wrapper<2, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithUnion(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    aDouble = arg.move();
    __isset.aDouble = true;
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithUnion(
    ::apache::thrift::detail::argument_wrapper<3, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithUnion(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    f = arg.move();
    __isset.f = true;
  }

  StructWithUnion(const StructWithUnion&);
  StructWithUnion& operator=(const StructWithUnion& src) {
    StructWithUnion tmp(src);
    swap(*this, tmp);
    return *this;
  }
  StructWithUnion(StructWithUnion&&) = default;
  StructWithUnion& operator=(StructWithUnion&&) = default;

  void __clear();

  virtual ~StructWithUnion() throw() {}

  std::unique_ptr<MyUnion> u;
  double aDouble;
  MyField f;

  struct __isset {
    __isset() { __clear(); } 
    void __clear() {
      aDouble = false;
      f = false;
    }
    bool aDouble;
    bool f;
  } __isset;

  bool operator == (const StructWithUnion &) const;
  bool operator != (const StructWithUnion& rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const StructWithUnion & ) const;

  uint32_t read(apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(apache::thrift::protocol::TProtocol* oprot) const;

};

class StructWithUnion;
void merge(const StructWithUnion& from, StructWithUnion& to);
void merge(StructWithUnion&& from, StructWithUnion& to);
void swap(RecursiveStruct &a, RecursiveStruct &b);

class RecursiveStruct : public apache::thrift::TStructType<RecursiveStruct> {
 public:

  static const uint64_t _reflection_id = 2826922994162023308U;
  static void _reflection_register(::apache::thrift::reflection::Schema&);
  RecursiveStruct() {
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit RecursiveStruct(
    ::apache::thrift::detail::argument_wrapper<1, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    RecursiveStruct(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    mes = arg.move();
    __isset.mes = true;
  }

  RecursiveStruct(const RecursiveStruct&) = default;
  RecursiveStruct& operator=(const RecursiveStruct& src)= default;
  RecursiveStruct(RecursiveStruct&&) = default;
  RecursiveStruct& operator=(RecursiveStruct&&) = default;

  void __clear();

  virtual ~RecursiveStruct() throw() {}

  std::vector<RecursiveStruct>  mes;

  struct __isset {
    __isset() { __clear(); } 
    void __clear() {
      mes = false;
    }
    bool mes;
  } __isset;

  bool operator == (const RecursiveStruct &) const;
  bool operator != (const RecursiveStruct& rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const RecursiveStruct & ) const;

  uint32_t read(apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(apache::thrift::protocol::TProtocol* oprot) const;

};

class RecursiveStruct;
void merge(const RecursiveStruct& from, RecursiveStruct& to);
void merge(RecursiveStruct&& from, RecursiveStruct& to);
void swap(StructWithContainers &a, StructWithContainers &b);

class StructWithContainers : public apache::thrift::TStructType<StructWithContainers> {
 public:

  static const uint64_t _reflection_id = 18101585657679500556U;
  static void _reflection_register(::apache::thrift::reflection::Schema&);
  StructWithContainers() {
    list_ref.reset(new typename decltype(list_ref)::element_type());
    set_ref.reset(new typename decltype(set_ref)::element_type());
    map_ref.reset(new typename decltype(map_ref)::element_type());
    list_ref_unique.reset(new typename decltype(list_ref_unique)::element_type());
    set_ref_shared.reset(new typename decltype(set_ref_shared)::element_type());
    map_ref_custom.reset(new typename decltype(map_ref_custom)::element_type());
    list_ref_shared_const.reset(new typename decltype(list_ref_shared_const)::element_type());
    set_custom_ref.reset(new typename decltype(set_custom_ref)::element_type());
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithContainers(
    ::apache::thrift::detail::argument_wrapper<1, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithContainers(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    list_ref = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithContainers(
    ::apache::thrift::detail::argument_wrapper<2, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithContainers(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    set_ref = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithContainers(
    ::apache::thrift::detail::argument_wrapper<3, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithContainers(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    map_ref = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithContainers(
    ::apache::thrift::detail::argument_wrapper<4, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithContainers(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    list_ref_unique = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithContainers(
    ::apache::thrift::detail::argument_wrapper<5, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithContainers(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    set_ref_shared = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithContainers(
    ::apache::thrift::detail::argument_wrapper<6, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithContainers(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    map_ref_custom = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithContainers(
    ::apache::thrift::detail::argument_wrapper<7, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithContainers(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    list_ref_shared_const = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithContainers(
    ::apache::thrift::detail::argument_wrapper<8, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithContainers(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    set_custom_ref = arg.move();
  }

  StructWithContainers(const StructWithContainers&);
  StructWithContainers& operator=(const StructWithContainers& src) {
    StructWithContainers tmp(src);
    swap(*this, tmp);
    return *this;
  }
  StructWithContainers(StructWithContainers&&) = default;
  StructWithContainers& operator=(StructWithContainers&&) = default;

  void __clear();

  virtual ~StructWithContainers() throw() {}

  std::unique_ptr<std::vector<int32_t> > list_ref;
  std::unique_ptr<std::set<int32_t> > set_ref;
  std::unique_ptr<std::map<int32_t, int32_t> > map_ref;
  std::unique_ptr<std::vector<int32_t> > list_ref_unique;
  std::shared_ptr<std::set<int32_t> > set_ref_shared;
  std::shared_ptr<const std::map<int32_t, int32_t>> map_ref_custom;
  std::shared_ptr<const std::vector<int32_t> > list_ref_shared_const;
  std::unique_ptr<std::set<int32_t> > set_custom_ref;

  struct __isset {
    __isset() { __clear(); } 
    void __clear() {
    }
  } __isset;

  bool operator == (const StructWithContainers &) const;
  bool operator != (const StructWithContainers& rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const StructWithContainers & ) const;

  uint32_t read(apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(apache::thrift::protocol::TProtocol* oprot) const;

};

class StructWithContainers;
void merge(const StructWithContainers& from, StructWithContainers& to);
void merge(StructWithContainers&& from, StructWithContainers& to);
void swap(StructWithSharedConst &a, StructWithSharedConst &b);

class StructWithSharedConst : public apache::thrift::TStructType<StructWithSharedConst> {
 public:

  static const uint64_t _reflection_id = 17232433652683371404U;
  static void _reflection_register(::apache::thrift::reflection::Schema&);
  StructWithSharedConst() {
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithSharedConst(
    ::apache::thrift::detail::argument_wrapper<1, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithSharedConst(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    opt_shared_const = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithSharedConst(
    ::apache::thrift::detail::argument_wrapper<2, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithSharedConst(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    shared_const = arg.move();
  }
  template <
    typename T__ThriftWrappedArgument__Ctor,
    typename... Args__ThriftWrappedArgument__Ctor
  >
  explicit StructWithSharedConst(
    ::apache::thrift::detail::argument_wrapper<3, T__ThriftWrappedArgument__Ctor> arg,
    Args__ThriftWrappedArgument__Ctor&&... args
  ):
    StructWithSharedConst(std::forward<Args__ThriftWrappedArgument__Ctor>(args)...)
  {
    req_shared_const = arg.move();
  }

  StructWithSharedConst(const StructWithSharedConst&) = default;
  StructWithSharedConst& operator=(const StructWithSharedConst& src)= default;
  StructWithSharedConst(StructWithSharedConst&&) = default;
  StructWithSharedConst& operator=(StructWithSharedConst&&) = default;

  void __clear();

  virtual ~StructWithSharedConst() throw() {}

  std::shared_ptr<const MyField> opt_shared_const;
  std::shared_ptr<const MyField> shared_const;
  std::shared_ptr<const MyField> req_shared_const;

  struct __isset {
    __isset() { __clear(); } 
    void __clear() {
    }
  } __isset;

  bool operator == (const StructWithSharedConst &) const;
  bool operator != (const StructWithSharedConst& rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const StructWithSharedConst & ) const;

  uint32_t read(apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(apache::thrift::protocol::TProtocol* oprot) const;

};

class StructWithSharedConst;
void merge(const StructWithSharedConst& from, StructWithSharedConst& to);
void merge(StructWithSharedConst&& from, StructWithSharedConst& to);


