

#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import abc as _abc
import typing as _typing
import builtins as _fbthrift_builtins



import folly.iobuf as _fbthrift_iobuf
import thrift.python.abstract_types as _fbthrift_python_abstract_types

class Foo(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def MyInt(self) -> int: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.namespace_from_package.module.thrift_mutable_types.Foo": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.namespace_from_package.module.thrift_types.Foo": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.namespace_from_package.module.types.Foo": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "namespace_from_package.module.ttypes.Foo": ...  # type: ignore
_fbthrift_Foo = Foo
