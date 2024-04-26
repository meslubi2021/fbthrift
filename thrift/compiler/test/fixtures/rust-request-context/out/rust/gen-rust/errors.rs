// @generated by Thrift for thrift/compiler/test/fixtures/rust-request-context/src/module.thrift
// This file is probably not the place you want to edit!

//! Thrift error definitions for `module`.

/// Error definitions for `MyInteraction`.
pub mod my_interaction {

    pub type PingError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_interaction::PingExn> for PingError {
        fn from(e: crate::services::my_interaction::PingExn) -> Self {
            match e {
                crate::services::my_interaction::PingExn::ApplicationException(aexn) =>
                    PingError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum PingReader {}

}

/// Error definitions for `MyService`.
pub mod my_service {

    pub type PingError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::PingExn> for PingError {
        fn from(e: crate::services::my_service::PingExn) -> Self {
            match e {
                crate::services::my_service::PingExn::ApplicationException(aexn) =>
                    PingError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum PingReader {}

    pub type GetRandomDataError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::GetRandomDataExn> for GetRandomDataError {
        fn from(e: crate::services::my_service::GetRandomDataExn) -> Self {
            match e {
                crate::services::my_service::GetRandomDataExn::ApplicationException(aexn) =>
                    GetRandomDataError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum GetRandomDataReader {}

    pub type HasDataByIdError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::HasDataByIdExn> for HasDataByIdError {
        fn from(e: crate::services::my_service::HasDataByIdExn) -> Self {
            match e {
                crate::services::my_service::HasDataByIdExn::ApplicationException(aexn) =>
                    HasDataByIdError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum HasDataByIdReader {}

    pub type GetDataByIdError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::GetDataByIdExn> for GetDataByIdError {
        fn from(e: crate::services::my_service::GetDataByIdExn) -> Self {
            match e {
                crate::services::my_service::GetDataByIdExn::ApplicationException(aexn) =>
                    GetDataByIdError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum GetDataByIdReader {}

    pub type PutDataByIdError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::PutDataByIdExn> for PutDataByIdError {
        fn from(e: crate::services::my_service::PutDataByIdExn) -> Self {
            match e {
                crate::services::my_service::PutDataByIdExn::ApplicationException(aexn) =>
                    PutDataByIdError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum PutDataByIdReader {}

    pub type LobDataByIdError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::LobDataByIdExn> for LobDataByIdError {
        fn from(e: crate::services::my_service::LobDataByIdExn) -> Self {
            match e {
                crate::services::my_service::LobDataByIdExn::ApplicationException(aexn) =>
                    LobDataByIdError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum LobDataByIdReader {}

    pub type StreamByIdError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::StreamByIdExn> for StreamByIdError {
        fn from(e: crate::services::my_service::StreamByIdExn) -> Self {
            match e {
                crate::services::my_service::StreamByIdExn::ApplicationException(aexn) =>
                    StreamByIdError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum StreamByIdReader {}

    pub type StreamByIdStreamError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::StreamByIdStreamExn> for StreamByIdStreamError {
        fn from(e: crate::services::my_service::StreamByIdStreamExn) -> Self {
            match e {
                crate::services::my_service::StreamByIdStreamExn::ApplicationException(aexn) =>
                    StreamByIdStreamError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum StreamByIdStreamReader {}

    pub type StreamByIdWithExceptionError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::StreamByIdWithExceptionExn> for StreamByIdWithExceptionError {
        fn from(e: crate::services::my_service::StreamByIdWithExceptionExn) -> Self {
            match e {
                crate::services::my_service::StreamByIdWithExceptionExn::ApplicationException(aexn) =>
                    StreamByIdWithExceptionError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum StreamByIdWithExceptionReader {}

    #[derive(Debug)]
    pub enum StreamByIdWithExceptionStreamError {
        e(crate::types::MyException),
        ApplicationException(::fbthrift::ApplicationException),
        ThriftError(::anyhow::Error),
    }

    /// Human-readable string representation of the Thrift client error.
    ///
    /// By default, this will not print the full cause chain. If you would like to print the underlying error
    /// cause, either use `format!("{:?}", anyhow::Error::from(client_err))` or print this using the
    /// alternate formatter `{:#}` instead of just `{}`.
    impl ::std::fmt::Display for StreamByIdWithExceptionStreamError {
        fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::result::Result<(), ::std::fmt::Error> {
            match self {
                Self::e(inner) => {
                    if f.alternate() {
                        write!(f, "MyService::streamByIdWithException failed with variant `e`: {:#}", inner)?;
                    } else {
                        write!(f, "MyService::streamByIdWithException failed with e(MyException)")?;
                    }
                }
                Self::ApplicationException(inner) => {
                    write!(f, "MyService::streamByIdWithException failed with ApplicationException")?;

                    if f.alternate() {
                      write!(f, ": {:#}", inner)?;
                    }
                }
                Self::ThriftError(inner) => {
                    write!(f, "MyService::streamByIdWithException failed with ThriftError")?;

                    if f.alternate() {
                      write!(f, ": {:#}", inner)?;
                    }
                }
            }

            Ok(())
        }
    }

    impl ::std::error::Error for StreamByIdWithExceptionStreamError {
        fn source(&self) -> ::std::option::Option<&(dyn ::std::error::Error + 'static)> {
            match self {
                Self::e(ref inner) => {
                    Some(inner)
                }
                Self::ApplicationException(ref inner) => {
                    Some(inner)
                }
                Self::ThriftError(ref inner) => {
                    Some(inner.as_ref())
                }
            }
        }
    }

    impl ::std::convert::From<crate::types::MyException> for StreamByIdWithExceptionStreamError {
        fn from(e: crate::types::MyException) -> Self {
            Self::e(e)
        }
    }

    impl ::std::convert::From<::anyhow::Error> for StreamByIdWithExceptionStreamError {
        fn from(err: ::anyhow::Error) -> Self {
            Self::ThriftError(err)
        }
    }

    impl ::std::convert::From<::fbthrift::ApplicationException> for StreamByIdWithExceptionStreamError {
        fn from(ae: ::fbthrift::ApplicationException) -> Self {
            Self::ApplicationException(ae)
        }
    }

    impl ::std::convert::From<crate::services::my_service::StreamByIdWithExceptionStreamExn> for StreamByIdWithExceptionStreamError {
        fn from(e: crate::services::my_service::StreamByIdWithExceptionStreamExn) -> Self {
            match e {
                crate::services::my_service::StreamByIdWithExceptionStreamExn::ApplicationException(aexn) =>
                    StreamByIdWithExceptionStreamError::ApplicationException(aexn),
                crate::services::my_service::StreamByIdWithExceptionStreamExn::e(exn) =>
                    StreamByIdWithExceptionStreamError::e(exn),
            }
        }
    }

    #[doc(hidden)]
    pub enum StreamByIdWithExceptionStreamReader {}

    pub type StreamByIdWithResponseError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::StreamByIdWithResponseExn> for StreamByIdWithResponseError {
        fn from(e: crate::services::my_service::StreamByIdWithResponseExn) -> Self {
            match e {
                crate::services::my_service::StreamByIdWithResponseExn::ApplicationException(aexn) =>
                    StreamByIdWithResponseError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum StreamByIdWithResponseReader {}

    pub type StreamByIdWithResponseStreamError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::StreamByIdWithResponseStreamExn> for StreamByIdWithResponseStreamError {
        fn from(e: crate::services::my_service::StreamByIdWithResponseStreamExn) -> Self {
            match e {
                crate::services::my_service::StreamByIdWithResponseStreamExn::ApplicationException(aexn) =>
                    StreamByIdWithResponseStreamError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum StreamByIdWithResponseStreamReader {}

    pub type StartPingInteractionError = ::fbthrift::NonthrowingFunctionError;

    impl ::std::convert::From<crate::services::my_service::StartPingInteractionExn> for StartPingInteractionError {
        fn from(e: crate::services::my_service::StartPingInteractionExn) -> Self {
            match e {
                crate::services::my_service::StartPingInteractionExn::ApplicationException(aexn) =>
                    StartPingInteractionError::ApplicationException(aexn),
            }
        }
    }

    #[doc(hidden)]
    pub enum StartPingInteractionReader {}

}

