

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


import enum as _enum


import folly.iobuf as _fbthrift_iobuf
import thrift.python.abstract_types as _fbthrift_python_abstract_types
import apache.thrift.type.id.thrift_abstract_types as _fbthrift__apache__thrift__type__id__thrift_abstract_types
import apache.thrift.type.schema.thrift_abstract_types as _fbthrift__apache__thrift__type__schema__thrift_abstract_types
import test.fixtures.python_capi.serialized_dep.thrift_abstract_types as _fbthrift__test__fixtures__python_capi__serialized_dep__thrift_abstract_types
import test.fixtures.python_capi.thrift_dep.thrift_abstract_types as _fbthrift__test__fixtures__python_capi__thrift_dep__thrift_abstract_types

from test.fixtures.python_capi.module.thrift_enums import (
    MyEnum,
    MyEnum as _fbthrift_MyEnum,
    _fbthrift_compatible_with_MyEnum,
    AnnoyingEnum,
    AnnoyingEnum as _fbthrift_AnnoyingEnum,
    _fbthrift_compatible_with_AnnoyingEnum,
)

class MyStruct(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def inty(self) -> int: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def stringy(self) -> str: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def myItemy(self) -> _fbthrift_MyDataItem: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def myEnumy(self) -> _fbthrift_MyEnum: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def booly(self) -> bool: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def floatListy(self) -> _typing.Sequence[float]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def strMappy(self) -> _typing.Mapping[bytes, str]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def intSetty(self) -> _typing.AbstractSet[int]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, str, _fbthrift_MyDataItem, _fbthrift_MyEnum, bool, _typing.Sequence[float], _typing.Mapping[bytes, str], _typing.AbstractSet[int]]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.MyStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.MyStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MyStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.MyStruct": ...  # type: ignore
_fbthrift_MyStruct = MyStruct
class MyDataItem(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def s(self) -> str: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.MyDataItem": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.MyDataItem": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MyDataItem": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.MyDataItem": ...  # type: ignore
_fbthrift_MyDataItem = MyDataItem
class TransitiveDoubler(_abc.ABC):
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.TransitiveDoubler": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.TransitiveDoubler": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.TransitiveDoubler": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.TransitiveDoubler": ...  # type: ignore
_fbthrift_TransitiveDoubler = TransitiveDoubler
class DoubledPair(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def s(self) -> str: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def x(self) -> int: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.DoubledPair": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.DoubledPair": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.DoubledPair": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.DoubledPair": ...  # type: ignore
_fbthrift_DoubledPair = DoubledPair
class StringPair(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def normal(self) -> str: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def doubled(self) -> str: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.StringPair": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.StringPair": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.StringPair": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.StringPair": ...  # type: ignore
_fbthrift_StringPair = StringPair
class EmptyStruct(_abc.ABC):
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.EmptyStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.EmptyStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.EmptyStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.EmptyStruct": ...  # type: ignore
_fbthrift_EmptyStruct = EmptyStruct
class PrimitiveStruct(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def booly(self) -> bool: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def charry(self) -> int: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def shorty(self) -> int: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def inty(self) -> int: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def longy(self) -> int: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def floaty(self) -> _typing.Optional[float]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def dubby(self) -> _typing.Optional[float]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def stringy(self) -> _typing.Optional[str]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def bytey(self) -> _typing.Optional[bytes]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def buffy(self) -> _fbthrift_iobuf.IOBuf: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def pointbuffy(self) -> _fbthrift_iobuf.IOBuf: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def patched_struct(self) -> _fbthrift_MyStruct: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def empty_struct(self) -> _fbthrift_EmptyStruct: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def fbstring(self) -> bytes: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def managed_string_view(self) -> str: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def some_error(self) -> _fbthrift__test__fixtures__python_capi__thrift_dep__thrift_abstract_types.SomeError: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, int, int, int, float, float, str, bytes, _fbthrift_iobuf.IOBuf, _fbthrift_iobuf.IOBuf, _fbthrift_MyStruct, _fbthrift_EmptyStruct, bytes, str, _fbthrift__test__fixtures__python_capi__thrift_dep__thrift_abstract_types.SomeError]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.PrimitiveStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.PrimitiveStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.PrimitiveStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.PrimitiveStruct": ...  # type: ignore
_fbthrift_PrimitiveStruct = PrimitiveStruct
class AdaptedFields(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def adapted_int(self) -> int: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def list_adapted_int(self) -> _typing.Sequence[int]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def set_adapted_int(self) -> _typing.AbstractSet[int]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def inline_adapted_int(self) -> int: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, _typing.Sequence[int], _typing.AbstractSet[int], int]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.AdaptedFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.AdaptedFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.AdaptedFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.AdaptedFields": ...  # type: ignore
_fbthrift_AdaptedFields = AdaptedFields
class ListStruct(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def boolz(self) -> _typing.Sequence[bool]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def intz(self) -> _typing.Optional[_typing.Sequence[int]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def stringz(self) -> _typing.Optional[_typing.Sequence[str]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def encoded(self) -> _typing.Sequence[bytes]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def uidz(self) -> _typing.Sequence[int]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def matrix(self) -> _typing.Sequence[_typing.Sequence[float]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def ucharz(self) -> _typing.Sequence[_typing.Sequence[int]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def voxels(self) -> _typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def buf_ptrs(self) -> _typing.Sequence[_fbthrift_iobuf.IOBuf]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.Sequence[bool], _typing.Sequence[int], _typing.Sequence[str], _typing.Sequence[bytes], _typing.Sequence[int], _typing.Sequence[_typing.Sequence[float]], _typing.Sequence[_typing.Sequence[int]], _typing.Sequence[_typing.Sequence[_typing.Sequence[int]]], _typing.Sequence[_fbthrift_iobuf.IOBuf]]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.ListStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.ListStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.ListStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.ListStruct": ...  # type: ignore
_fbthrift_ListStruct = ListStruct
class SetStruct(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def enumz(self) -> _typing.AbstractSet[_fbthrift_MyEnum]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def intz(self) -> _typing.Optional[_typing.AbstractSet[int]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def binnaz(self) -> _typing.Optional[_typing.AbstractSet[bytes]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def encoded(self) -> _typing.AbstractSet[bytes]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def uidz(self) -> _typing.AbstractSet[int]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def charz(self) -> _typing.AbstractSet[int]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def setz(self) -> _typing.Sequence[_typing.AbstractSet[int]]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.AbstractSet[_fbthrift_MyEnum], _typing.AbstractSet[int], _typing.AbstractSet[bytes], _typing.AbstractSet[bytes], _typing.AbstractSet[int], _typing.AbstractSet[int], _typing.Sequence[_typing.AbstractSet[int]]]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.SetStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.SetStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.SetStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.SetStruct": ...  # type: ignore
_fbthrift_SetStruct = SetStruct
class MapStruct(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def enumz(self) -> _typing.Mapping[_fbthrift_MyEnum, str]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def intz(self) -> _typing.Optional[_typing.Mapping[int, str]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def binnaz(self) -> _typing.Optional[_typing.Mapping[bytes, _fbthrift_PrimitiveStruct]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def encoded(self) -> _typing.Mapping[str, float]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def flotz(self) -> _typing.Mapping[int, float]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def map_list(self) -> _typing.Sequence[_typing.Mapping[int, int]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def list_map(self) -> _typing.Mapping[int, _typing.Sequence[int]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def fast_list_map(self) -> _typing.Mapping[int, _typing.Sequence[float]]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def buf_map(self) -> _typing.Mapping[bytes, _fbthrift_iobuf.IOBuf]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def unsigned_list_map(self) -> _typing.Mapping[int, _typing.Sequence[int]]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.Mapping[_fbthrift_MyEnum, str], _typing.Mapping[int, str], _typing.Mapping[bytes, _fbthrift_PrimitiveStruct], _typing.Mapping[str, float], _typing.Mapping[int, float], _typing.Sequence[_typing.Mapping[int, int]], _typing.Mapping[int, _typing.Sequence[int]], _typing.Mapping[int, _typing.Sequence[float]], _typing.Mapping[bytes, _fbthrift_iobuf.IOBuf], _typing.Mapping[int, _typing.Sequence[int]]]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.MapStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.MapStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MapStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.MapStruct": ...  # type: ignore
_fbthrift_MapStruct = MapStruct
class ComposeStruct(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def enum_(self) -> _fbthrift_MyEnum: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def renamed_(self) -> _fbthrift_AnnoyingEnum: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def primitive(self) -> _fbthrift_PrimitiveStruct: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def aliased(self) -> _fbthrift_ListStruct: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def xenum(self) -> _fbthrift__test__fixtures__python_capi__thrift_dep__thrift_abstract_types.DepEnum: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def xstruct(self) -> _fbthrift__test__fixtures__python_capi__thrift_dep__thrift_abstract_types.DepStruct: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def friends(self) -> _typing.Sequence[_fbthrift__test__fixtures__python_capi__thrift_dep__thrift_abstract_types.DepStruct]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def serial_struct(self) -> _fbthrift__test__fixtures__python_capi__serialized_dep__thrift_abstract_types.SerializedStruct: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def serial_union(self) -> _fbthrift__test__fixtures__python_capi__serialized_dep__thrift_abstract_types.SerializedUnion: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def serial_error(self) -> _fbthrift__test__fixtures__python_capi__serialized_dep__thrift_abstract_types.SerializedError: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_fbthrift_MyEnum, _fbthrift_AnnoyingEnum, _fbthrift_PrimitiveStruct, _fbthrift_ListStruct, _fbthrift__test__fixtures__python_capi__thrift_dep__thrift_abstract_types.DepEnum, _fbthrift__test__fixtures__python_capi__thrift_dep__thrift_abstract_types.DepStruct, _typing.Sequence[_fbthrift__test__fixtures__python_capi__thrift_dep__thrift_abstract_types.DepStruct], _fbthrift__test__fixtures__python_capi__serialized_dep__thrift_abstract_types.SerializedStruct, _fbthrift__test__fixtures__python_capi__serialized_dep__thrift_abstract_types.SerializedUnion, _fbthrift__test__fixtures__python_capi__serialized_dep__thrift_abstract_types.SerializedError]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.ComposeStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.ComposeStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.ComposeStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.ComposeStruct": ...  # type: ignore
_fbthrift_ComposeStruct = ComposeStruct
class Onion(_abc.ABC):
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def myEnum(self) -> _fbthrift_MyEnum: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def myStruct(self) -> _fbthrift_PrimitiveStruct: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def myString(self) -> str: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def intSet(self) -> _typing.AbstractSet[int]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def doubleList(self) -> _typing.Sequence[float]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def strMap(self) -> _typing.Mapping[bytes, str]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def adapted_int(self) -> int: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.module.thrift_mutable_types.Onion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.Onion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.Onion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.Onion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        myEnum = 1
        myStruct = 2
        myString = 4
        intSet = 6
        doubleList = 8
        strMap = 9
        adapted_int = 10

    FbThriftUnionFieldEnum.__name__ = "Onion"
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def fbthrift_current_value(self) -> _typing.Union[None, _fbthrift_MyEnum, _fbthrift_PrimitiveStruct, str, _typing.AbstractSet[int], _typing.Sequence[float], _typing.Mapping[bytes, str], int]: ...
    # pyre-ignore[16]: Module `_fbthrift_builtins` has no attribute `property`.
    @_fbthrift_builtins.property
    @_abc.abstractmethod
    def fbthrift_current_field(self) -> FbThriftUnionFieldEnum: ...

_fbthrift_Onion = Onion

uint64 = int
ui64 = int
signed_byte = int
IOBuf = _fbthrift_iobuf.IOBuf
IOBufPtr = _fbthrift_iobuf.IOBuf
ListAlias = _fbthrift_ListStruct
