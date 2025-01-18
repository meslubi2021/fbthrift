

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
import foo.thrift_abstract_types as _fbthrift__foo__thrift_abstract_types

class Fields(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def injected_field(self) -> str: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Fields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.Fields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.Fields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.Fields": ...  # type: ignore
_fbthrift_Fields = Fields
class FieldsInjectedToEmptyStruct(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def injected_field(self) -> str: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.FieldsInjectedToEmptyStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.FieldsInjectedToEmptyStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.FieldsInjectedToEmptyStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.FieldsInjectedToEmptyStruct": ...  # type: ignore
_fbthrift_FieldsInjectedToEmptyStruct = FieldsInjectedToEmptyStruct
class FieldsInjectedToStruct(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def injected_field(self) -> str: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def string_field(self) -> str: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.FieldsInjectedToStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.FieldsInjectedToStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.FieldsInjectedToStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.FieldsInjectedToStruct": ...  # type: ignore
_fbthrift_FieldsInjectedToStruct = FieldsInjectedToStruct
class FieldsInjectedWithIncludedStruct(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def injected_unstructured_annotation_field(self) -> _typing.Optional[str]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def injected_structured_annotation_field(self) -> _typing.Optional[str]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def injected_field(self) -> str: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def string_field(self) -> str: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str, str, str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.FieldsInjectedWithIncludedStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.FieldsInjectedWithIncludedStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.FieldsInjectedWithIncludedStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.FieldsInjectedWithIncludedStruct": ...  # type: ignore
_fbthrift_FieldsInjectedWithIncludedStruct = FieldsInjectedWithIncludedStruct
