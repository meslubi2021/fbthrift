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
import test.fixtures.interactions.module.thrift_abstract_types as _fbthrift_python_abstract_types
import thrift.python.types as _fbthrift_python_types
import thrift.python.mutable_types as _fbthrift_python_mutable_types
import thrift.python.mutable_exceptions as _fbthrift_python_mutable_exceptions
import thrift.python.mutable_containers as _fbthrift_python_mutable_containers

import test.fixtures.another_interactions.shared.thrift_mutable_types as _fbthrift__test__fixtures__another_interactions__shared__thrift_mutable_types


class _fbthrift_compatible_with_CustomException:
    pass


class CustomException(_fbthrift_python_mutable_exceptions.MutableGeneratedError, _fbthrift_compatible_with_CustomException, _fbthrift_python_abstract_types.CustomException):

    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str) -> None: ...

    def __init__(
        self, *,
        message: _typing.Optional[str]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> "test.fixtures.interactions.module.thrift_types.CustomException": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.interactions.module.types.CustomException": ...  # type: ignore
    def _to_py_deprecated(self) -> "test.fixtures.interactions.ttypes.CustomException": ...  # type: ignore
_fbthrift_CustomException = CustomException

class _fbthrift_compatible_with_ShouldBeBoxed:
    pass


class ShouldBeBoxed(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_ShouldBeBoxed, _fbthrift_python_abstract_types.ShouldBeBoxed):

    @property
    def sessionId(self) -> str: ...
    @sessionId.setter
    def sessionId(self, value: str) -> None: ...

    def __init__(
        self, *,
        sessionId: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        sessionId: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> "test.fixtures.interactions.module.thrift_types.ShouldBeBoxed": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.interactions.module.types.ShouldBeBoxed": ...  # type: ignore
    def _to_py_deprecated(self) -> "test.fixtures.interactions.ttypes.ShouldBeBoxed": ...  # type: ignore
_fbthrift_ShouldBeBoxed = ShouldBeBoxed


class _fbthrift_MyService_foo_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyService_foo_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyService_interact_args(_fbthrift_python_mutable_types.MutableStruct):
    arg: _typing.Final[int] = ...

    def __init__(
        self, *,
        arg: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, int]]]: ...


class _fbthrift_MyService_interact_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyService_interactFast_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyService_interactFast_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_MyService_serialize_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyService_serialize_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_MyService_serialize_result_stream(_fbthrift_python_mutable_types._fbthrift_MutableResponseStreamResult[int]):

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_MyInteraction_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]
    ex: _typing.Final[_fbthrift_CustomException]

    def __init__(
        self, *, success: _typing.Optional[int] = ..., ex: _typing.Optional[_fbthrift_CustomException]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
            _fbthrift_CustomException,
        ]]]: ...


class _fbthrift_MyInteraction_ping_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_truthify_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_truthify_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyInteraction_truthify_result_stream(_fbthrift_python_mutable_types._fbthrift_MutableResponseStreamResult[bool]):

    def __init__(
        self, *, success: _typing.Optional[bool] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bool,
        ]]]: ...


class _fbthrift_MyInteractionFast_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteractionFast_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_MyInteractionFast_ping_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteractionFast_truthify_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteractionFast_truthify_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyInteractionFast_truthify_result_stream(_fbthrift_python_mutable_types._fbthrift_MutableResponseStreamResult[bool]):

    def __init__(
        self, *, success: _typing.Optional[bool] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bool,
        ]]]: ...


class _fbthrift_SerialInteraction_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SerialInteraction_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_Factories_foo_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_Factories_foo_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_Factories_interact_args(_fbthrift_python_mutable_types.MutableStruct):
    arg: _typing.Final[int] = ...

    def __init__(
        self, *,
        arg: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, int]]]: ...


class _fbthrift_Factories_interact_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_Factories_interactFast_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_Factories_interactFast_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_Factories_serialize_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_Factories_serialize_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_Factories_serialize_result_stream(_fbthrift_python_mutable_types._fbthrift_MutableResponseStreamResult[int]):

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_MyInteraction_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]
    ex: _typing.Final[_fbthrift_CustomException]

    def __init__(
        self, *, success: _typing.Optional[int] = ..., ex: _typing.Optional[_fbthrift_CustomException]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
            _fbthrift_CustomException,
        ]]]: ...


class _fbthrift_MyInteraction_ping_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_truthify_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_truthify_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyInteraction_truthify_result_stream(_fbthrift_python_mutable_types._fbthrift_MutableResponseStreamResult[bool]):

    def __init__(
        self, *, success: _typing.Optional[bool] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bool,
        ]]]: ...


class _fbthrift_MyInteractionFast_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteractionFast_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_MyInteractionFast_ping_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteractionFast_truthify_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteractionFast_truthify_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyInteractionFast_truthify_result_stream(_fbthrift_python_mutable_types._fbthrift_MutableResponseStreamResult[bool]):

    def __init__(
        self, *, success: _typing.Optional[bool] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bool,
        ]]]: ...


class _fbthrift_SerialInteraction_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SerialInteraction_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_Perform_foo_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_Perform_foo_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyInteraction_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]
    ex: _typing.Final[_fbthrift_CustomException]

    def __init__(
        self, *, success: _typing.Optional[int] = ..., ex: _typing.Optional[_fbthrift_CustomException]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
            _fbthrift_CustomException,
        ]]]: ...


class _fbthrift_MyInteraction_ping_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_truthify_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_truthify_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyInteraction_truthify_result_stream(_fbthrift_python_mutable_types._fbthrift_MutableResponseStreamResult[bool]):

    def __init__(
        self, *, success: _typing.Optional[bool] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bool,
        ]]]: ...


class _fbthrift_MyInteractionFast_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteractionFast_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_MyInteractionFast_ping_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteractionFast_truthify_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteractionFast_truthify_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyInteractionFast_truthify_result_stream(_fbthrift_python_mutable_types._fbthrift_MutableResponseStreamResult[bool]):

    def __init__(
        self, *, success: _typing.Optional[bool] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bool,
        ]]]: ...


class _fbthrift_SerialInteraction_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SerialInteraction_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_InteractWithShared_do_some_similar_things_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_InteractWithShared_do_some_similar_things_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[_fbthrift__test__fixtures__another_interactions__shared__thrift_mutable_types.DoSomethingResult]

    def __init__(
        self, *, success: _typing.Optional[_fbthrift__test__fixtures__another_interactions__shared__thrift_mutable_types.DoSomethingResult] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _fbthrift__test__fixtures__another_interactions__shared__thrift_mutable_types.DoSomethingResult,
        ]]]: ...


class _fbthrift_MyInteraction_frobnicate_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_frobnicate_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]
    ex: _typing.Final[_fbthrift_CustomException]

    def __init__(
        self, *, success: _typing.Optional[int] = ..., ex: _typing.Optional[_fbthrift_CustomException]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
            _fbthrift_CustomException,
        ]]]: ...


class _fbthrift_MyInteraction_ping_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_truthify_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_MyInteraction_truthify_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyInteraction_truthify_result_stream(_fbthrift_python_mutable_types._fbthrift_MutableResponseStreamResult[bool]):

    def __init__(
        self, *, success: _typing.Optional[bool] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bool,
        ]]]: ...


class _fbthrift_SharedInteraction_init_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SharedInteraction_init_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SharedInteraction_do_something_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SharedInteraction_do_something_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[_fbthrift__test__fixtures__another_interactions__shared__thrift_mutable_types.DoSomethingResult]

    def __init__(
        self, *, success: _typing.Optional[_fbthrift__test__fixtures__another_interactions__shared__thrift_mutable_types.DoSomethingResult] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _fbthrift__test__fixtures__another_interactions__shared__thrift_mutable_types.DoSomethingResult,
        ]]]: ...


class _fbthrift_SharedInteraction_tear_down_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SharedInteraction_tear_down_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_BoxService_getABoxSession_args(_fbthrift_python_mutable_types.MutableStruct):
    req: _typing.Final[_fbthrift_ShouldBeBoxed] = ...

    def __init__(
        self, *,
        req: _typing.Optional[_fbthrift_ShouldBeBoxed]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _fbthrift_ShouldBeBoxed]]]: ...


class _fbthrift_BoxService_getABoxSession_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[_fbthrift_ShouldBeBoxed]

    def __init__(
        self, *, success: _typing.Optional[_fbthrift_ShouldBeBoxed] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _fbthrift_ShouldBeBoxed,
        ]]]: ...


class _fbthrift_BoxedInteraction_getABox_args(_fbthrift_python_mutable_types.MutableStruct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_BoxedInteraction_getABox_result(_fbthrift_python_mutable_types.MutableStruct):
    success: _typing.Final[_fbthrift_ShouldBeBoxed]

    def __init__(
        self, *, success: _typing.Optional[_fbthrift_ShouldBeBoxed] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _fbthrift_ShouldBeBoxed,
        ]]]: ...
