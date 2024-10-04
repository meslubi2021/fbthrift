#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations


# EXPERIMENTAL - DO NOT USE !!!
# See `experimental_generate_mutable_types` documentation in thrift compiler

#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import typing as _typing

import enum

import folly.iobuf as _fbthrift_iobuf
import thrift.python.types as _fbthrift_python_types
import thrift.python.mutable_types as _fbthrift_python_mutable_types
import thrift.python.mutable_exceptions as _fbthrift_python_mutable_exceptions

import apache.thrift.type.id.thrift_types

import apache.thrift.type.schema.thrift_types

import test.fixtures.python_capi.serialized_dep.thrift_types

import test.fixtures.python_capi.thrift_dep.thrift_types

class _fbthrift_compatible_with_MyEnum:
    pass


class MyEnum(_fbthrift_python_types.Enum, int, _fbthrift_compatible_with_MyEnum):
    MyValue1: MyEnum = ...
    MyValue2: MyEnum = ...
    def _to_python(self) -> MyEnum: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MyEnum": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...

class _fbthrift_compatible_with_AnnoyingEnum:
    pass


class AnnoyingEnum(_fbthrift_python_types.Enum, int, _fbthrift_compatible_with_AnnoyingEnum):
    FOO: AnnoyingEnum = ...
    BAR: AnnoyingEnum = ...
    def _to_python(self) -> AnnoyingEnum: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.AnnoyingEnum": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...


class _fbthrift_compatible_with_MyStruct:
    pass


class MyStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_MyStruct):
    inty: int = ...
    stringy: str = ...
    myItemy: MyDataItem = ...
    myEnumy: MyEnum = ...
    booly: bool = ...
    floatListy: _typing.MutableSequence[float] = ...
    strMappy: _typing.MutableMapping[bytes, str] = ...
    intSetty: _typing.MutableSet[int] = ...
    def __init__(
        self, *,
        inty: _typing.Optional[int]=...,
        stringy: _typing.Optional[str]=...,
        myItemy: _typing.Optional[_fbthrift_compatible_with_MyDataItem]=...,
        myEnumy: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        booly: _typing.Optional[bool]=...,
        floatListy: _typing.Optional[_typing.MutableSequence[float]]=...,
        strMappy: _typing.Optional[_typing.MutableMapping[bytes, str]]=...,
        intSetty: _typing.Optional[_typing.MutableSet[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        inty: _typing.Optional[int]=...,
        stringy: _typing.Optional[str]=...,
        myItemy: _typing.Optional[_fbthrift_compatible_with_MyDataItem]=...,
        myEnumy: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        booly: _typing.Optional[bool]=...,
        floatListy: _typing.Optional[_typing.MutableSequence[float]]=...,
        strMappy: _typing.Optional[_typing.MutableMapping[bytes, str]]=...,
        intSetty: _typing.Optional[_typing.MutableSet[int]]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, str, MyDataItem, MyEnum, bool, _typing.MutableSequence[float], _typing.MutableMapping[bytes, str], _typing.MutableSet[int]]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.MyStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStruct": ...  # type: ignore


class _fbthrift_compatible_with_MyDataItem:
    pass


class MyDataItem(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_MyDataItem):
    s: str = ...
    def __init__(
        self, *,
        s: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        s: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.MyDataItem": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MyDataItem": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyDataItem": ...  # type: ignore


class _fbthrift_compatible_with_TransitiveDoubler:
    pass


class TransitiveDoubler(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_TransitiveDoubler):
    def __init__(
        self,
    ) -> None: ...

    def __call__(
        self,
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.TransitiveDoubler": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.TransitiveDoubler": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.TransitiveDoubler": ...  # type: ignore


class _fbthrift_compatible_with_DoubledPair:
    pass


class DoubledPair(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_DoubledPair):
    s: str = ...
    x: int = ...
    def __init__(
        self, *,
        s: _typing.Optional[str]=...,
        x: _typing.Optional[int]=...
    ) -> None: ...

    def __call__(
        self, *,
        s: _typing.Optional[str]=...,
        x: _typing.Optional[int]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.DoubledPair": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.DoubledPair": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.DoubledPair": ...  # type: ignore


class _fbthrift_compatible_with_StringPair:
    pass


class StringPair(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_StringPair):
    normal: str = ...
    doubled: str = ...
    def __init__(
        self, *,
        normal: _typing.Optional[str]=...,
        doubled: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        normal: _typing.Optional[str]=...,
        doubled: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.StringPair": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.StringPair": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.StringPair": ...  # type: ignore


class _fbthrift_compatible_with_EmptyStruct:
    pass


class EmptyStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_EmptyStruct):
    def __init__(
        self,
    ) -> None: ...

    def __call__(
        self,
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.EmptyStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.EmptyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.EmptyStruct": ...  # type: ignore


class _fbthrift_compatible_with_PrimitiveStruct:
    pass


class PrimitiveStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_PrimitiveStruct):
    booly: bool = ...
    charry: int = ...
    shorty: int = ...
    inty: int = ...
    longy: int = ...
    floaty: _typing.Optional[float] = ...
    dubby: _typing.Optional[float] = ...
    stringy: _typing.Optional[str] = ...
    bytey: _typing.Optional[bytes] = ...
    buffy: _fbthrift_iobuf.IOBuf = ...
    pointbuffy: _fbthrift_iobuf.IOBuf = ...
    patched_struct: MyStruct = ...
    empty_struct: EmptyStruct = ...
    fbstring: bytes = ...
    managed_string_view: str = ...
    some_error: test.fixtures.python_capi.thrift_dep.thrift_mutable_types.SomeError = ...
    def __init__(
        self, *,
        booly: _typing.Optional[bool]=...,
        charry: _typing.Optional[int]=...,
        shorty: _typing.Optional[int]=...,
        inty: _typing.Optional[int]=...,
        longy: _typing.Optional[int]=...,
        floaty: _typing.Optional[float]=...,
        dubby: _typing.Optional[float]=...,
        stringy: _typing.Optional[str]=...,
        bytey: _typing.Optional[bytes]=...,
        buffy: _typing.Optional[_fbthrift_iobuf.IOBuf]=...,
        pointbuffy: _typing.Optional[_fbthrift_iobuf.IOBuf]=...,
        patched_struct: _typing.Optional[_fbthrift_compatible_with_MyStruct]=...,
        empty_struct: _typing.Optional[_fbthrift_compatible_with_EmptyStruct]=...,
        fbstring: _typing.Optional[bytes]=...,
        managed_string_view: _typing.Optional[str]=...,
        some_error: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_SomeError]=...
    ) -> None: ...

    def __call__(
        self, *,
        booly: _typing.Optional[bool]=...,
        charry: _typing.Optional[int]=...,
        shorty: _typing.Optional[int]=...,
        inty: _typing.Optional[int]=...,
        longy: _typing.Optional[int]=...,
        floaty: _typing.Optional[float]=...,
        dubby: _typing.Optional[float]=...,
        stringy: _typing.Optional[str]=...,
        bytey: _typing.Optional[bytes]=...,
        buffy: _typing.Optional[_fbthrift_iobuf.IOBuf]=...,
        pointbuffy: _typing.Optional[_fbthrift_iobuf.IOBuf]=...,
        patched_struct: _typing.Optional[_fbthrift_compatible_with_MyStruct]=...,
        empty_struct: _typing.Optional[_fbthrift_compatible_with_EmptyStruct]=...,
        fbstring: _typing.Optional[bytes]=...,
        managed_string_view: _typing.Optional[str]=...,
        some_error: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_SomeError]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, int, int, int, float, float, str, bytes, _fbthrift_iobuf.IOBuf, _fbthrift_iobuf.IOBuf, MyStruct, EmptyStruct, bytes, str, test.fixtures.python_capi.thrift_dep.thrift_mutable_types.SomeError]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.PrimitiveStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.PrimitiveStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.PrimitiveStruct": ...  # type: ignore


class _fbthrift_compatible_with_AdaptedFields:
    pass


class AdaptedFields(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_AdaptedFields):
    adapted_int: int = ...
    list_adapted_int: _typing.MutableSequence[int] = ...
    set_adapted_int: _typing.MutableSet[int] = ...
    inline_adapted_int: int = ...
    def __init__(
        self, *,
        adapted_int: _typing.Optional[int]=...,
        list_adapted_int: _typing.Optional[_typing.MutableSequence[int]]=...,
        set_adapted_int: _typing.Optional[_typing.MutableSet[int]]=...,
        inline_adapted_int: _typing.Optional[int]=...
    ) -> None: ...

    def __call__(
        self, *,
        adapted_int: _typing.Optional[int]=...,
        list_adapted_int: _typing.Optional[_typing.MutableSequence[int]]=...,
        set_adapted_int: _typing.Optional[_typing.MutableSet[int]]=...,
        inline_adapted_int: _typing.Optional[int]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, _typing.MutableSequence[int], _typing.MutableSet[int], int]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.AdaptedFields": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.AdaptedFields": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.AdaptedFields": ...  # type: ignore


class _fbthrift_compatible_with_ListStruct:
    pass


class ListStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_ListStruct):
    boolz: _typing.MutableSequence[bool] = ...
    intz: _typing.Optional[_typing.MutableSequence[int]] = ...
    stringz: _typing.Optional[_typing.MutableSequence[str]] = ...
    encoded: _typing.MutableSequence[bytes] = ...
    uidz: _typing.MutableSequence[int] = ...
    matrix: _typing.MutableSequence[_typing.MutableSequence[float]] = ...
    ucharz: _typing.MutableSequence[_typing.MutableSequence[int]] = ...
    voxels: _typing.MutableSequence[_typing.MutableSequence[_typing.MutableSequence[int]]] = ...
    buf_ptrs: _typing.MutableSequence[_fbthrift_iobuf.IOBuf] = ...
    def __init__(
        self, *,
        boolz: _typing.Optional[_typing.MutableSequence[bool]]=...,
        intz: _typing.Optional[_typing.MutableSequence[int]]=...,
        stringz: _typing.Optional[_typing.MutableSequence[str]]=...,
        encoded: _typing.Optional[_typing.MutableSequence[bytes]]=...,
        uidz: _typing.Optional[_typing.MutableSequence[int]]=...,
        matrix: _typing.Optional[_typing.MutableSequence[_typing.MutableSequence[float]]]=...,
        ucharz: _typing.Optional[_typing.MutableSequence[_typing.MutableSequence[int]]]=...,
        voxels: _typing.Optional[_typing.MutableSequence[_typing.MutableSequence[_typing.MutableSequence[int]]]]=...,
        buf_ptrs: _typing.Optional[_typing.MutableSequence[_fbthrift_iobuf.IOBuf]]=...
    ) -> None: ...

    def __call__(
        self, *,
        boolz: _typing.Optional[_typing.MutableSequence[bool]]=...,
        intz: _typing.Optional[_typing.MutableSequence[int]]=...,
        stringz: _typing.Optional[_typing.MutableSequence[str]]=...,
        encoded: _typing.Optional[_typing.MutableSequence[bytes]]=...,
        uidz: _typing.Optional[_typing.MutableSequence[int]]=...,
        matrix: _typing.Optional[_typing.MutableSequence[_typing.MutableSequence[float]]]=...,
        ucharz: _typing.Optional[_typing.MutableSequence[_typing.MutableSequence[int]]]=...,
        voxels: _typing.Optional[_typing.MutableSequence[_typing.MutableSequence[_typing.MutableSequence[int]]]]=...,
        buf_ptrs: _typing.Optional[_typing.MutableSequence[_fbthrift_iobuf.IOBuf]]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.MutableSequence[bool], _typing.MutableSequence[int], _typing.MutableSequence[str], _typing.MutableSequence[bytes], _typing.MutableSequence[int], _typing.MutableSequence[_typing.MutableSequence[float]], _typing.MutableSequence[_typing.MutableSequence[int]], _typing.MutableSequence[_typing.MutableSequence[_typing.MutableSequence[int]]], _typing.MutableSequence[_fbthrift_iobuf.IOBuf]]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.ListStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.ListStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ListStruct": ...  # type: ignore


class _fbthrift_compatible_with_SetStruct:
    pass


class SetStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_SetStruct):
    enumz: _typing.MutableSet[MyEnum] = ...
    intz: _typing.Optional[_typing.MutableSet[int]] = ...
    binnaz: _typing.Optional[_typing.MutableSet[bytes]] = ...
    encoded: _typing.MutableSet[bytes] = ...
    uidz: _typing.MutableSet[int] = ...
    charz: _typing.MutableSet[int] = ...
    setz: _typing.MutableSequence[_typing.MutableSet[int]] = ...
    def __init__(
        self, *,
        enumz: _typing.Optional[_typing.MutableSet[_fbthrift_compatible_with_MyEnum]]=...,
        intz: _typing.Optional[_typing.MutableSet[int]]=...,
        binnaz: _typing.Optional[_typing.MutableSet[bytes]]=...,
        encoded: _typing.Optional[_typing.MutableSet[bytes]]=...,
        uidz: _typing.Optional[_typing.MutableSet[int]]=...,
        charz: _typing.Optional[_typing.MutableSet[int]]=...,
        setz: _typing.Optional[_typing.MutableSequence[_typing.MutableSet[int]]]=...
    ) -> None: ...

    def __call__(
        self, *,
        enumz: _typing.Optional[_typing.MutableSet[_fbthrift_compatible_with_MyEnum]]=...,
        intz: _typing.Optional[_typing.MutableSet[int]]=...,
        binnaz: _typing.Optional[_typing.MutableSet[bytes]]=...,
        encoded: _typing.Optional[_typing.MutableSet[bytes]]=...,
        uidz: _typing.Optional[_typing.MutableSet[int]]=...,
        charz: _typing.Optional[_typing.MutableSet[int]]=...,
        setz: _typing.Optional[_typing.MutableSequence[_typing.MutableSet[int]]]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.MutableSet[MyEnum], _typing.MutableSet[int], _typing.MutableSet[bytes], _typing.MutableSet[bytes], _typing.MutableSet[int], _typing.MutableSet[int], _typing.MutableSequence[_typing.MutableSet[int]]]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.SetStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.SetStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.SetStruct": ...  # type: ignore


class _fbthrift_compatible_with_MapStruct:
    pass


class MapStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_MapStruct):
    enumz: _typing.MutableMapping[MyEnum, str] = ...
    intz: _typing.Optional[_typing.MutableMapping[int, str]] = ...
    binnaz: _typing.Optional[_typing.MutableMapping[bytes, PrimitiveStruct]] = ...
    encoded: _typing.MutableMapping[str, float] = ...
    flotz: _typing.MutableMapping[int, float] = ...
    map_list: _typing.MutableSequence[_typing.MutableMapping[int, int]] = ...
    list_map: _typing.MutableMapping[int, _typing.MutableSequence[int]] = ...
    fast_list_map: _typing.MutableMapping[int, _typing.MutableSequence[float]] = ...
    buf_map: _typing.MutableMapping[bytes, _fbthrift_iobuf.IOBuf] = ...
    unsigned_list_map: _typing.MutableMapping[int, _typing.MutableSequence[int]] = ...
    def __init__(
        self, *,
        enumz: _typing.Optional[_typing.MutableMapping[MyEnum, str]]=...,
        intz: _typing.Optional[_typing.MutableMapping[int, str]]=...,
        binnaz: _typing.Optional[_typing.MutableMapping[bytes, _fbthrift_compatible_with_PrimitiveStruct]]=...,
        encoded: _typing.Optional[_typing.MutableMapping[str, float]]=...,
        flotz: _typing.Optional[_typing.MutableMapping[int, float]]=...,
        map_list: _typing.Optional[_typing.MutableSequence[_typing.MutableMapping[int, int]]]=...,
        list_map: _typing.Optional[_typing.MutableMapping[int, _typing.MutableSequence[int]]]=...,
        fast_list_map: _typing.Optional[_typing.MutableMapping[int, _typing.MutableSequence[float]]]=...,
        buf_map: _typing.Optional[_typing.MutableMapping[bytes, _fbthrift_iobuf.IOBuf]]=...,
        unsigned_list_map: _typing.Optional[_typing.MutableMapping[int, _typing.MutableSequence[int]]]=...
    ) -> None: ...

    def __call__(
        self, *,
        enumz: _typing.Optional[_typing.MutableMapping[MyEnum, str]]=...,
        intz: _typing.Optional[_typing.MutableMapping[int, str]]=...,
        binnaz: _typing.Optional[_typing.MutableMapping[bytes, _fbthrift_compatible_with_PrimitiveStruct]]=...,
        encoded: _typing.Optional[_typing.MutableMapping[str, float]]=...,
        flotz: _typing.Optional[_typing.MutableMapping[int, float]]=...,
        map_list: _typing.Optional[_typing.MutableSequence[_typing.MutableMapping[int, int]]]=...,
        list_map: _typing.Optional[_typing.MutableMapping[int, _typing.MutableSequence[int]]]=...,
        fast_list_map: _typing.Optional[_typing.MutableMapping[int, _typing.MutableSequence[float]]]=...,
        buf_map: _typing.Optional[_typing.MutableMapping[bytes, _fbthrift_iobuf.IOBuf]]=...,
        unsigned_list_map: _typing.Optional[_typing.MutableMapping[int, _typing.MutableSequence[int]]]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.MutableMapping[MyEnum, str], _typing.MutableMapping[int, str], _typing.MutableMapping[bytes, PrimitiveStruct], _typing.MutableMapping[str, float], _typing.MutableMapping[int, float], _typing.MutableSequence[_typing.MutableMapping[int, int]], _typing.MutableMapping[int, _typing.MutableSequence[int]], _typing.MutableMapping[int, _typing.MutableSequence[float]], _typing.MutableMapping[bytes, _fbthrift_iobuf.IOBuf], _typing.MutableMapping[int, _typing.MutableSequence[int]]]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.MapStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MapStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MapStruct": ...  # type: ignore


class _fbthrift_compatible_with_ComposeStruct:
    pass


class ComposeStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_ComposeStruct):
    enum_: MyEnum = ...
    renamed_: AnnoyingEnum = ...
    primitive: PrimitiveStruct = ...
    aliased: ListStruct = ...
    xenum: test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepEnum = ...
    xstruct: test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepStruct = ...
    friends: _typing.MutableSequence[test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepStruct] = ...
    serial_struct: test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedStruct = ...
    serial_union: test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedUnion = ...
    serial_error: test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedError = ...
    def __init__(
        self, *,
        enum_: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        renamed_: _typing.Optional[_fbthrift_compatible_with_AnnoyingEnum]=...,
        primitive: _typing.Optional[_fbthrift_compatible_with_PrimitiveStruct]=...,
        aliased: _typing.Optional[_fbthrift_compatible_with_ListStruct]=...,
        xenum: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepEnum]=...,
        xstruct: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepStruct]=...,
        friends: _typing.Optional[_typing.MutableSequence[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepStruct]]=...,
        serial_struct: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedStruct]=...,
        serial_union: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedUnion]=...,
        serial_error: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedError]=...
    ) -> None: ...

    def __call__(
        self, *,
        enum_: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        renamed_: _typing.Optional[_fbthrift_compatible_with_AnnoyingEnum]=...,
        primitive: _typing.Optional[_fbthrift_compatible_with_PrimitiveStruct]=...,
        aliased: _typing.Optional[_fbthrift_compatible_with_ListStruct]=...,
        xenum: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepEnum]=...,
        xstruct: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepStruct]=...,
        friends: _typing.Optional[_typing.MutableSequence[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepStruct]]=...,
        serial_struct: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedStruct]=...,
        serial_union: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedUnion]=...,
        serial_error: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedError]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[MyEnum, AnnoyingEnum, PrimitiveStruct, ListStruct, test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepEnum, test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepStruct, _typing.MutableSequence[test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepStruct], test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedStruct, test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedUnion, test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedError]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.ComposeStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.ComposeStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ComposeStruct": ...  # type: ignore


class _fbthrift_compatible_with_Onion:
    pass


class Onion(_fbthrift_python_mutable_types.MutableUnion, _fbthrift_compatible_with_Onion):
    myEnum: MyEnum = ...
    myStruct: PrimitiveStruct = ...
    myString: str = ...
    intSet: _typing.MutableSet[int] = ...
    doubleList: _typing.MutableSequence[float] = ...
    strMap: _typing.MutableMapping[bytes, str] = ...
    adapted_int: int = ...
    def __init__(
        self, *,
        myEnum: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        myStruct: _typing.Optional[_fbthrift_compatible_with_PrimitiveStruct]=...,
        myString: _typing.Optional[str]=...,
        intSet: _typing.Optional[_typing.MutableSet[int]]=...,
        doubleList: _typing.Optional[_typing.MutableSequence[float]]=...,
        strMap: _typing.Optional[_typing.MutableMapping[bytes, str]]=...,
        adapted_int: _typing.Optional[int]=...
    ) -> None: ...


    class FbThriftUnionFieldEnum(enum.Enum):
        EMPTY: Onion.FbThriftUnionFieldEnum = ...
        myEnum: Onion.Type = ...
        myStruct: Onion.Type = ...
        myString: Onion.Type = ...
        intSet: Onion.Type = ...
        doubleList: Onion.Type = ...
        strMap: Onion.Type = ...
        adapted_int: Onion.Type = ...

    fbthrift_current_value: _typing.Final[_typing.Union[None, MyEnum, PrimitiveStruct, str, _typing.MutableSet[int], _typing.MutableSequence[float], _typing.MutableMapping[bytes, str], int]]
    fbthrift_current_field: FbThriftUnionFieldEnum
    def get_type(self) -> FbThriftUnionFieldEnum:...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.Onion": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.Onion": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Onion": ...  # type: ignore

uint64 = int
ui64 = int
signed_byte = int
IOBuf = _fbthrift_iobuf.IOBuf
IOBufPtr = _fbthrift_iobuf.IOBuf
ListAlias = ListStruct
