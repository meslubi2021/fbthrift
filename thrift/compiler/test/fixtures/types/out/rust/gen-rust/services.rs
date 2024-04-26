// @generated by Thrift for thrift/compiler/test/fixtures/types/src/module.thrift
// This file is probably not the place you want to edit!

//! Thrift service definitions for `module`.


/// Service definitions for `SomeService`.
pub mod some_service {
    #[derive(Clone, Debug)]
    pub enum BounceMapExn {

        ApplicationException(::fbthrift::ApplicationException),
    }

    impl ::std::convert::From<crate::errors::some_service::BounceMapError> for BounceMapExn {
        fn from(err: crate::errors::some_service::BounceMapError) -> Self {
            match err {
                crate::errors::some_service::BounceMapError::ApplicationException(aexn) => BounceMapExn::ApplicationException(aexn),
                crate::errors::some_service::BounceMapError::ThriftError(err) => BounceMapExn::ApplicationException(::fbthrift::ApplicationException {
                    message: err.to_string(),
                    type_: ::fbthrift::ApplicationExceptionErrorCode::InternalError,
                }),
            }
        }
    }

    impl ::std::convert::From<::fbthrift::ApplicationException> for BounceMapExn {
        fn from(exn: ::fbthrift::ApplicationException) -> Self {
            Self::ApplicationException(exn)
        }
    }

    impl ::fbthrift::ExceptionInfo for BounceMapExn {
        fn exn_name(&self) -> &'static str {
            match self {
                Self::ApplicationException(aexn) => aexn.exn_name(),
            }
        }

        fn exn_value(&self) -> String {
            match self {
                Self::ApplicationException(aexn) => aexn.exn_value(),
            }
        }

        fn exn_is_declared(&self) -> bool {
            match self {
                Self::ApplicationException(aexn) => aexn.exn_is_declared(),
            }
        }
    }

    impl ::fbthrift::ResultInfo for BounceMapExn {
        fn result_type(&self) -> ::fbthrift::ResultType {
            match self {
                Self::ApplicationException(_aexn) => ::fbthrift::ResultType::Exception,
            }
        }
    }

    impl<P> ::fbthrift::Serialize<P> for BounceMapExn
    where
        P: ::fbthrift::ProtocolWriter,
    {
        fn write(&self, p: &mut P) {
            ::fbthrift::help::SerializeExn::write_result(Err(self), p);
        }
    }

    impl ::fbthrift::help::SerializeExn for BounceMapExn {
        type Success = included__types::SomeMap;

        fn write_result<P>(res: ::std::result::Result<&Self::Success, &Self>, p: &mut P)
        where
            P: ::fbthrift::ProtocolWriter,
        {
            if let ::std::result::Result::Err(Self::ApplicationException(aexn)) = res {
                ::fbthrift::Serialize::write(aexn, p);
                return;
            }
            p.write_struct_begin("BounceMap");
            match res {
                ::std::result::Result::Ok(_success) => {
                    p.write_field_begin("Success", ::fbthrift::TType::Map, 0i16);
                    ::fbthrift::Serialize::write(_success, p);
                    p.write_field_end();
                }

                ::std::result::Result::Err(Self::ApplicationException(_aexn)) => unreachable!(),
            }
            p.write_field_stop();
            p.write_struct_end();
        }
    }

    impl ::fbthrift::help::DeserializeExn for crate::errors::some_service::BounceMapReader {
        type Success = included__types::SomeMap;
        type Error = crate::errors::some_service::BounceMapError;

        fn read_result<P>(p: &mut P) -> ::anyhow::Result<::std::result::Result<Self::Success, Self::Error>>
        where
            P: ::fbthrift::ProtocolReader,
        {
            static RETURNS: &[::fbthrift::Field] = &[
                ::fbthrift::Field::new("Success", ::fbthrift::TType::Map, 0),
            ];
            let _ = p.read_struct_begin(|_| ())?;
            let mut once = false;
            let mut alt = ::std::option::Option::None;
            loop {
                let (_, fty, fid) = p.read_field_begin(|_| (), RETURNS)?;
                match ((fty, fid as ::std::primitive::i32), once) {
                    ((::fbthrift::TType::Stop, _), _) => {
                        p.read_field_end()?;
                        break;
                    }
                    ((::fbthrift::TType::Map, 0i32), false) => {
                        once = true;
                        alt = ::std::option::Option::Some(::std::result::Result::Ok(::fbthrift::Deserialize::read(p)?));
                    }
                    ((ty, _id), false) => p.skip(ty)?,
                    ((badty, badid), true) => return ::std::result::Result::Err(::std::convert::From::from(
                        ::fbthrift::ApplicationException::new(
                            ::fbthrift::ApplicationExceptionErrorCode::ProtocolError,
                            format!(
                                "unwanted extra union {} field ty {:?} id {}",
                                "BounceMapError",
                                badty,
                                badid,
                            ),
                        )
                    )),
                }
                p.read_field_end()?;
            }
            p.read_struct_end()?;
            alt.ok_or_else(||
                ::fbthrift::ApplicationException::new(
                    ::fbthrift::ApplicationExceptionErrorCode::MissingResult,
                    format!("Empty union {}", "BounceMapError"),
                )
                .into(),
            )
        }
    }

    #[derive(Clone, Debug)]
    pub enum BinaryKeyedMapExn {

        ApplicationException(::fbthrift::ApplicationException),
    }

    impl ::std::convert::From<crate::errors::some_service::BinaryKeyedMapError> for BinaryKeyedMapExn {
        fn from(err: crate::errors::some_service::BinaryKeyedMapError) -> Self {
            match err {
                crate::errors::some_service::BinaryKeyedMapError::ApplicationException(aexn) => BinaryKeyedMapExn::ApplicationException(aexn),
                crate::errors::some_service::BinaryKeyedMapError::ThriftError(err) => BinaryKeyedMapExn::ApplicationException(::fbthrift::ApplicationException {
                    message: err.to_string(),
                    type_: ::fbthrift::ApplicationExceptionErrorCode::InternalError,
                }),
            }
        }
    }

    impl ::std::convert::From<::fbthrift::ApplicationException> for BinaryKeyedMapExn {
        fn from(exn: ::fbthrift::ApplicationException) -> Self {
            Self::ApplicationException(exn)
        }
    }

    impl ::fbthrift::ExceptionInfo for BinaryKeyedMapExn {
        fn exn_name(&self) -> &'static str {
            match self {
                Self::ApplicationException(aexn) => aexn.exn_name(),
            }
        }

        fn exn_value(&self) -> String {
            match self {
                Self::ApplicationException(aexn) => aexn.exn_value(),
            }
        }

        fn exn_is_declared(&self) -> bool {
            match self {
                Self::ApplicationException(aexn) => aexn.exn_is_declared(),
            }
        }
    }

    impl ::fbthrift::ResultInfo for BinaryKeyedMapExn {
        fn result_type(&self) -> ::fbthrift::ResultType {
            match self {
                Self::ApplicationException(_aexn) => ::fbthrift::ResultType::Exception,
            }
        }
    }

    impl<P> ::fbthrift::Serialize<P> for BinaryKeyedMapExn
    where
        P: ::fbthrift::ProtocolWriter,
    {
        fn write(&self, p: &mut P) {
            ::fbthrift::help::SerializeExn::write_result(Err(self), p);
        }
    }

    impl ::fbthrift::help::SerializeExn for BinaryKeyedMapExn {
        type Success = ::std::collections::BTreeMap<crate::types::TBinary, ::std::primitive::i64>;

        fn write_result<P>(res: ::std::result::Result<&Self::Success, &Self>, p: &mut P)
        where
            P: ::fbthrift::ProtocolWriter,
        {
            if let ::std::result::Result::Err(Self::ApplicationException(aexn)) = res {
                ::fbthrift::Serialize::write(aexn, p);
                return;
            }
            p.write_struct_begin("BinaryKeyedMap");
            match res {
                ::std::result::Result::Ok(_success) => {
                    p.write_field_begin("Success", ::fbthrift::TType::Map, 0i16);
                    ::fbthrift::Serialize::write(_success, p);
                    p.write_field_end();
                }

                ::std::result::Result::Err(Self::ApplicationException(_aexn)) => unreachable!(),
            }
            p.write_field_stop();
            p.write_struct_end();
        }
    }

    impl ::fbthrift::help::DeserializeExn for crate::errors::some_service::BinaryKeyedMapReader {
        type Success = ::std::collections::BTreeMap<crate::types::TBinary, ::std::primitive::i64>;
        type Error = crate::errors::some_service::BinaryKeyedMapError;

        fn read_result<P>(p: &mut P) -> ::anyhow::Result<::std::result::Result<Self::Success, Self::Error>>
        where
            P: ::fbthrift::ProtocolReader,
        {
            static RETURNS: &[::fbthrift::Field] = &[
                ::fbthrift::Field::new("Success", ::fbthrift::TType::Map, 0),
            ];
            let _ = p.read_struct_begin(|_| ())?;
            let mut once = false;
            let mut alt = ::std::option::Option::None;
            loop {
                let (_, fty, fid) = p.read_field_begin(|_| (), RETURNS)?;
                match ((fty, fid as ::std::primitive::i32), once) {
                    ((::fbthrift::TType::Stop, _), _) => {
                        p.read_field_end()?;
                        break;
                    }
                    ((::fbthrift::TType::Map, 0i32), false) => {
                        once = true;
                        alt = ::std::option::Option::Some(::std::result::Result::Ok(::fbthrift::Deserialize::read(p)?));
                    }
                    ((ty, _id), false) => p.skip(ty)?,
                    ((badty, badid), true) => return ::std::result::Result::Err(::std::convert::From::from(
                        ::fbthrift::ApplicationException::new(
                            ::fbthrift::ApplicationExceptionErrorCode::ProtocolError,
                            format!(
                                "unwanted extra union {} field ty {:?} id {}",
                                "BinaryKeyedMapError",
                                badty,
                                badid,
                            ),
                        )
                    )),
                }
                p.read_field_end()?;
            }
            p.read_struct_end()?;
            alt.ok_or_else(||
                ::fbthrift::ApplicationException::new(
                    ::fbthrift::ApplicationExceptionErrorCode::MissingResult,
                    format!("Empty union {}", "BinaryKeyedMapError"),
                )
                .into(),
            )
        }
    }
}
