/**
 * Autogenerated by Thrift for src/extra_services.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated @nocommit
 */
#pragma once

#include  "thrift/compiler/test/fixtures/mcpp2-compare/gen-cpp2/module_fatal_types.h"

#include "thrift/compiler/test/fixtures/mcpp2-compare/gen-cpp2/extra_services_types.h"

#include "thrift/compiler/test/fixtures/mcpp2-compare/gen-cpp2/extra_services_fatal.h"

#include <fatal/type/traits.h>
#include <fatal/type/list.h>

namespace extra { namespace svc {

namespace __fbthrift_refl {
namespace __fbthrift_refl_impl = ::apache::thrift::detail::reflection_impl;

class containerStruct2_struct_traits {
  class __fbthrift_annotations : public __fbthrift_refl_impl::no_annotations {
    class __fbthrift_members {
     public:
      using fieldA = __fbthrift_refl_impl::reflected_no_annotations;
      using req_fieldA = __fbthrift_refl_impl::reflected_no_annotations;
      using opt_fieldA = __fbthrift_refl_impl::reflected_no_annotations;
      using fieldB = __fbthrift_refl_impl::reflected_no_annotations;
      using req_fieldB = __fbthrift_refl_impl::reflected_no_annotations;
      using opt_fieldB = __fbthrift_refl_impl::reflected_no_annotations;
      using fieldC = __fbthrift_refl_impl::reflected_no_annotations;
      using req_fieldC = __fbthrift_refl_impl::reflected_no_annotations;
      using opt_fieldC = __fbthrift_refl_impl::reflected_no_annotations;
      using fieldD = __fbthrift_refl_impl::reflected_no_annotations;
      using fieldE = __fbthrift_refl_impl::reflected_no_annotations;
      using req_fieldE = __fbthrift_refl_impl::reflected_no_annotations;
      using opt_fieldE = __fbthrift_refl_impl::reflected_no_annotations;
    };

   public:
    using members = __fbthrift_members;
  };

  struct __fbthrift_member_fieldA {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_a003c1938a10c7729197e235918bdad7bc795ec24b19f24c66e4f24374526ad8;
    using type = bool;
    using tag = ::apache::thrift::tag::fieldA;
    static constexpr ::apache::thrift::field_id_t id = 1;
    static constexpr auto optional = ::apache::thrift::optionality::required_of_writer;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::fieldA>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::fieldA>;
    using type_class = ::apache::thrift::type_class::integral;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::fieldA>;
  };
  struct __fbthrift_member_req_fieldA {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_5c3b94a8e304a4356159a39553a29b9ba5d46658be8683264a16f34ba323fbfc;
    using type = bool;
    using tag = ::apache::thrift::tag::req_fieldA;
    static constexpr ::apache::thrift::field_id_t id = 101;
    static constexpr auto optional = ::apache::thrift::optionality::required;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::req_fieldA>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::req_fieldA>;
    using type_class = ::apache::thrift::type_class::integral;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::req_fieldA>;
  };
  struct __fbthrift_member_opt_fieldA {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_19bdb7a3067217940c2b50b0b5221b2d567285f43296c6f40e62b2b860a6fe2b;
    using type = bool;
    using tag = ::apache::thrift::tag::opt_fieldA;
    static constexpr ::apache::thrift::field_id_t id = 201;
    static constexpr auto optional = ::apache::thrift::optionality::optional;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::opt_fieldA>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::opt_fieldA>;
    using type_class = ::apache::thrift::type_class::integral;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::opt_fieldA>;
  };
  struct __fbthrift_member_fieldB {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_c7e10d053d5c1a0a0743c1dfc0a38c439cd181cc30829f18cc684e286d0baf27;
    using type = ::std::map<::std::string, bool>;
    using tag = ::apache::thrift::tag::fieldB;
    static constexpr ::apache::thrift::field_id_t id = 2;
    static constexpr auto optional = ::apache::thrift::optionality::required_of_writer;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::fieldB>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::fieldB>;
    using type_class = ::apache::thrift::type_class::map<::apache::thrift::type_class::string, ::apache::thrift::type_class::integral>;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::fieldB>;
  };
  struct __fbthrift_member_req_fieldB {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_a93a0375706770237da363401aec269f1d6ad07d41bb42463ddd1c792185810c;
    using type = ::std::map<::std::string, bool>;
    using tag = ::apache::thrift::tag::req_fieldB;
    static constexpr ::apache::thrift::field_id_t id = 102;
    static constexpr auto optional = ::apache::thrift::optionality::required;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::req_fieldB>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::req_fieldB>;
    using type_class = ::apache::thrift::type_class::map<::apache::thrift::type_class::string, ::apache::thrift::type_class::integral>;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::req_fieldB>;
  };
  struct __fbthrift_member_opt_fieldB {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_5a736b7ef4c69ca7479ecf23288415bbeee1751449d5a26721ce85d0c810728c;
    using type = ::std::map<::std::string, bool>;
    using tag = ::apache::thrift::tag::opt_fieldB;
    static constexpr ::apache::thrift::field_id_t id = 202;
    static constexpr auto optional = ::apache::thrift::optionality::optional;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::opt_fieldB>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::opt_fieldB>;
    using type_class = ::apache::thrift::type_class::map<::apache::thrift::type_class::string, ::apache::thrift::type_class::integral>;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::opt_fieldB>;
  };
  struct __fbthrift_member_fieldC {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_7a60aa9f6a5416b61206a441ce84695a835326c0edc0c9b86b92b618f29eb9ed;
    using type = ::std::set<::std::int32_t>;
    using tag = ::apache::thrift::tag::fieldC;
    static constexpr ::apache::thrift::field_id_t id = 3;
    static constexpr auto optional = ::apache::thrift::optionality::required_of_writer;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::fieldC>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::fieldC>;
    using type_class = ::apache::thrift::type_class::set<::apache::thrift::type_class::integral>;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::fieldC>;
  };
  struct __fbthrift_member_req_fieldC {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_bf973e4523774cc2e393efe85aaeaecdfc90a464b96a36f42e93d457237aee7f;
    using type = ::std::set<::std::int32_t>;
    using tag = ::apache::thrift::tag::req_fieldC;
    static constexpr ::apache::thrift::field_id_t id = 103;
    static constexpr auto optional = ::apache::thrift::optionality::required;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::req_fieldC>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::req_fieldC>;
    using type_class = ::apache::thrift::type_class::set<::apache::thrift::type_class::integral>;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::req_fieldC>;
  };
  struct __fbthrift_member_opt_fieldC {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_ec9bc154cafd382fcf46ef9489c25b9df04efacf81018fcf5e4c7ce728f25a1c;
    using type = ::std::set<::std::int32_t>;
    using tag = ::apache::thrift::tag::opt_fieldC;
    static constexpr ::apache::thrift::field_id_t id = 203;
    static constexpr auto optional = ::apache::thrift::optionality::optional;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::opt_fieldC>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::opt_fieldC>;
    using type_class = ::apache::thrift::type_class::set<::apache::thrift::type_class::integral>;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::opt_fieldC>;
  };
  struct __fbthrift_member_fieldD {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_a73c4974ccb5981437f75c22da908dd553c1389729210c7d554a65e1b0f4045a;
    using type = ::std::string;
    using tag = ::apache::thrift::tag::fieldD;
    static constexpr ::apache::thrift::field_id_t id = 4;
    static constexpr auto optional = ::apache::thrift::optionality::required_of_writer;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::fieldD>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::fieldD>;
    using type_class = ::apache::thrift::type_class::string;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::fieldD>;
  };
  struct __fbthrift_member_fieldE {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_ba2a88de7258832d40bb04e70c8d37d66141754f3561ecfa366dc9496c9a7704;
    using type = ::std::string;
    using tag = ::apache::thrift::tag::fieldE;
    static constexpr ::apache::thrift::field_id_t id = 5;
    static constexpr auto optional = ::apache::thrift::optionality::required_of_writer;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::fieldE>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::fieldE>;
    using type_class = ::apache::thrift::type_class::string;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::fieldE>;
  };
  struct __fbthrift_member_req_fieldE {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_59ee7a3ea45725149c15fa11ce6bf5c8cc5336a3641edf62fd3265fdcab97bba;
    using type = ::std::string;
    using tag = ::apache::thrift::tag::req_fieldE;
    static constexpr ::apache::thrift::field_id_t id = 105;
    static constexpr auto optional = ::apache::thrift::optionality::required;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::req_fieldE>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::req_fieldE>;
    using type_class = ::apache::thrift::type_class::string;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::req_fieldE>;
  };
  struct __fbthrift_member_opt_fieldE {
    using owner = ::extra::svc::containerStruct2;
    using name = __fbthrift_strings_extra_services::__fbthrift_hash_d0ddd5cb59fc0d5c728d0572d06ad2305f2140665e2a75a4928198f7f678a0a6;
    using type = ::std::string;
    using tag = ::apache::thrift::tag::opt_fieldE;
    static constexpr ::apache::thrift::field_id_t id = 205;
    static constexpr auto optional = ::apache::thrift::optionality::optional;
    using getter = __fbthrift_refl_impl::data_member_accessor<::apache::thrift::tag::opt_fieldE>;
    using field_ref_getter = ::apache::thrift::detail::invoke_reffer<::apache::thrift::tag::opt_fieldE>;
    using type_class = ::apache::thrift::type_class::string;
    using annotations = ::apache::thrift::reflected_annotations<__fbthrift_annotations::members::opt_fieldE>;
  };

  struct __fbthrift_member {
    using fieldA = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_fieldA>;
    using req_fieldA = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_req_fieldA>;
    using opt_fieldA = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_opt_fieldA>;
    using fieldB = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_fieldB>;
    using req_fieldB = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_req_fieldB>;
    using opt_fieldB = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_opt_fieldB>;
    using fieldC = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_fieldC>;
    using req_fieldC = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_req_fieldC>;
    using opt_fieldC = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_opt_fieldC>;
    using fieldD = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_fieldD>;
    using fieldE = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_fieldE>;
    using req_fieldE = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_req_fieldE>;
    using opt_fieldE = ::apache::thrift::reflected_struct_data_member<__fbthrift_member_opt_fieldE>;
  };
 public:
  using type = ::extra::svc::containerStruct2;
  using name = __fbthrift_strings_extra_services::containerStruct2;
  using member = __fbthrift_member;
  using members = ::fatal::list<
      member::fieldA,
      member::req_fieldA,
      member::opt_fieldA,
      member::fieldB,
      member::req_fieldB,
      member::opt_fieldB,
      member::fieldC,
      member::req_fieldC,
      member::opt_fieldC,
      member::fieldD,
      member::fieldE,
      member::req_fieldE,
      member::opt_fieldE
  >;
  using members_annotations = __fbthrift_annotations::members;
  using metadata = ::apache::thrift::detail::type_common_metadata_impl<
      extra_services_tags::module,
      ::apache::thrift::reflected_annotations<__fbthrift_annotations>,
      static_cast<::apache::thrift::legacy_type_id_t>(14729324538950551532ull)
  >;
};

} // __fbthrift_refl

THRIFT_REGISTER_STRUCT_TRAITS(containerStruct2, __fbthrift_refl::containerStruct2_struct_traits);
}} // extra::svc
