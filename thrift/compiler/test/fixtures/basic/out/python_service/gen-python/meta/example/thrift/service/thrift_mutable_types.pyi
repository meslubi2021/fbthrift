#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations


# EXPERIMENTAL - DO NOT USE !!!

#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import typing as _typing

import folly.iobuf as _fbthrift_iobuf
import meta.example.thrift.service.thrift_abstract_types as _fbthrift_python_abstract_types
import thrift.python.types as _fbthrift_python_types
import thrift.python.mutable_types as _fbthrift_python_mutable_types
import thrift.python.mutable_exceptions as _fbthrift_python_mutable_exceptions
import thrift.python.mutable_containers as _fbthrift_python_mutable_containers


class _fbthrift_compatible_with_EchoRequest:
    pass


class EchoRequest(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_EchoRequest, _fbthrift_python_abstract_types.EchoRequest):

    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...

    def __init__(
        self, *,
        text: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        text: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> "meta.example.thrift.service.thrift_types.EchoRequest": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "meta.example.thrift.service.types.EchoRequest": ...  # type: ignore
    def _to_py_deprecated(self) -> "service.ttypes.EchoRequest": ...  # type: ignore
_fbthrift_EchoRequest = EchoRequest

class _fbthrift_compatible_with_EchoResponse:
    pass


class EchoResponse(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_EchoResponse, _fbthrift_python_abstract_types.EchoResponse):

    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...

    def __init__(
        self, *,
        text: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        text: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> "meta.example.thrift.service.thrift_types.EchoResponse": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "meta.example.thrift.service.types.EchoResponse": ...  # type: ignore
    def _to_py_deprecated(self) -> "service.ttypes.EchoResponse": ...  # type: ignore
_fbthrift_EchoResponse = EchoResponse

class _fbthrift_compatible_with_WhisperException:
    pass


class WhisperException(_fbthrift_python_mutable_exceptions.MutableGeneratedError, _fbthrift_compatible_with_WhisperException, _fbthrift_python_abstract_types.WhisperException):

    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str) -> None: ...

    def __init__(
        self, *,
        message: _typing.Optional[str]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> "meta.example.thrift.service.thrift_types.WhisperException": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "meta.example.thrift.service.types.WhisperException": ...  # type: ignore
    def _to_py_deprecated(self) -> "service.ttypes.WhisperException": ...  # type: ignore
_fbthrift_WhisperException = WhisperException


class _fbthrift_EchoService_echo_args(_fbthrift_python_mutable_types.MutableStruct):
    request: _typing.Final[_fbthrift_EchoRequest] = ...

    def __init__(
        self, *,
        request: _typing.Optional[_fbthrift_EchoRequest]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _fbthrift_EchoRequest]]]: ...


class _fbthrift_EchoService_echo_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[_fbthrift_EchoResponse]
    ex: _typing.Final[_fbthrift_WhisperException]

    def __init__(
        self, *, success: _typing.Optional[_fbthrift_EchoResponse] = ..., ex: _typing.Optional[_fbthrift_WhisperException]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _fbthrift_EchoResponse,
            _fbthrift_WhisperException,
        ]]]: ...
