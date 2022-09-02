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
import thrift.python.exceptions as _fbthrift_python_exceptions

import apache.thrift.op.patch.thrift_types

import facebook.thrift.annotation.thrift.thrift_types


class MyData(_fbthrift_python_types.Struct):
    data1: _typing.Final[str] = ...
    data2: _typing.Final[int] = ...
    def __init__(
        self, *,
        data1: _typing.Optional[str]=...,
        data2: _typing.Optional[int]=...
    ) -> None: ...

    def __call__(
        self, *,
        data1: _typing.Optional[str]=...,
        data2: _typing.Optional[int]=...
    ) -> MyData: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int]]]: ...
    def _to_python(self) -> MyData: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyData": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyData": ...  # type: ignore


class InnerUnion(_fbthrift_python_types.Union):
    innerOption: _typing.Final[bytes] = ...
    def __init__(
        self, *,
        innerOption: _typing.Optional[bytes]=...
    ) -> None: ...


    class Type(enum.Enum):
        EMPTY: InnerUnion.Type = ...
        innerOption: InnerUnion.Type = ...

    @classmethod
    def fromValue(cls, value: _typing.Union[None, bytes]) -> InnerUnion: ...
    value: _typing.Final[_typing.Union[None, bytes]]
    type: Type
    def get_type(self) -> Type:...
    def _to_python(self) -> InnerUnion: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.InnerUnion": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.InnerUnion": ...  # type: ignore


class MyUnion(_fbthrift_python_types.Union):
    option1: _typing.Final[str] = ...
    option2: _typing.Final[int] = ...
    option3: _typing.Final[InnerUnion] = ...
    def __init__(
        self, *,
        option1: _typing.Optional[str]=...,
        option2: _typing.Optional[int]=...,
        option3: _typing.Optional[InnerUnion]=...
    ) -> None: ...


    class Type(enum.Enum):
        EMPTY: MyUnion.Type = ...
        option1: MyUnion.Type = ...
        option2: MyUnion.Type = ...
        option3: MyUnion.Type = ...

    @classmethod
    def fromValue(cls, value: _typing.Union[None, str, int, InnerUnion]) -> MyUnion: ...
    value: _typing.Final[_typing.Union[None, str, int, InnerUnion]]
    type: Type
    def get_type(self) -> Type:...
    def _to_python(self) -> MyUnion: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyUnion": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyUnion": ...  # type: ignore


class MyStruct(_fbthrift_python_types.Struct):
    boolVal: _typing.Final[bool] = ...
    byteVal: _typing.Final[int] = ...
    i16Val: _typing.Final[int] = ...
    i32Val: _typing.Final[int] = ...
    i64Val: _typing.Final[int] = ...
    floatVal: _typing.Final[float] = ...
    doubleVal: _typing.Final[float] = ...
    stringVal: _typing.Final[str] = ...
    binaryVal: _typing.Final[bytes] = ...
    structVal: _typing.Final[MyData] = ...
    optBoolVal: _typing.Final[_typing.Optional[bool]] = ...
    optByteVal: _typing.Final[_typing.Optional[int]] = ...
    optI16Val: _typing.Final[_typing.Optional[int]] = ...
    optI32Val: _typing.Final[_typing.Optional[int]] = ...
    optI64Val: _typing.Final[_typing.Optional[int]] = ...
    optFloatVal: _typing.Final[_typing.Optional[float]] = ...
    optDoubleVal: _typing.Final[_typing.Optional[float]] = ...
    optStringVal: _typing.Final[_typing.Optional[str]] = ...
    optBinaryVal: _typing.Final[_typing.Optional[bytes]] = ...
    optStructVal: _typing.Final[_typing.Optional[MyData]] = ...
    optListVal: _typing.Final[_typing.Optional[_typing.Sequence[int]]] = ...
    optSetVal: _typing.Final[_typing.Optional[_typing.AbstractSet[str]]] = ...
    optMapVal: _typing.Final[_typing.Optional[_typing.Mapping[str, str]]] = ...
    unionVal: _typing.Final[MyUnion] = ...
    def __init__(
        self, *,
        boolVal: _typing.Optional[bool]=...,
        byteVal: _typing.Optional[int]=...,
        i16Val: _typing.Optional[int]=...,
        i32Val: _typing.Optional[int]=...,
        i64Val: _typing.Optional[int]=...,
        floatVal: _typing.Optional[float]=...,
        doubleVal: _typing.Optional[float]=...,
        stringVal: _typing.Optional[str]=...,
        binaryVal: _typing.Optional[bytes]=...,
        structVal: _typing.Optional[MyData]=...,
        optBoolVal: _typing.Optional[bool]=...,
        optByteVal: _typing.Optional[int]=...,
        optI16Val: _typing.Optional[int]=...,
        optI32Val: _typing.Optional[int]=...,
        optI64Val: _typing.Optional[int]=...,
        optFloatVal: _typing.Optional[float]=...,
        optDoubleVal: _typing.Optional[float]=...,
        optStringVal: _typing.Optional[str]=...,
        optBinaryVal: _typing.Optional[bytes]=...,
        optStructVal: _typing.Optional[MyData]=...,
        optListVal: _typing.Optional[_typing.Sequence[int]]=...,
        optSetVal: _typing.Optional[_typing.AbstractSet[str]]=...,
        optMapVal: _typing.Optional[_typing.Mapping[str, str]]=...,
        unionVal: _typing.Optional[MyUnion]=...
    ) -> None: ...

    def __call__(
        self, *,
        boolVal: _typing.Optional[bool]=...,
        byteVal: _typing.Optional[int]=...,
        i16Val: _typing.Optional[int]=...,
        i32Val: _typing.Optional[int]=...,
        i64Val: _typing.Optional[int]=...,
        floatVal: _typing.Optional[float]=...,
        doubleVal: _typing.Optional[float]=...,
        stringVal: _typing.Optional[str]=...,
        binaryVal: _typing.Optional[bytes]=...,
        structVal: _typing.Optional[MyData]=...,
        optBoolVal: _typing.Optional[bool]=...,
        optByteVal: _typing.Optional[int]=...,
        optI16Val: _typing.Optional[int]=...,
        optI32Val: _typing.Optional[int]=...,
        optI64Val: _typing.Optional[int]=...,
        optFloatVal: _typing.Optional[float]=...,
        optDoubleVal: _typing.Optional[float]=...,
        optStringVal: _typing.Optional[str]=...,
        optBinaryVal: _typing.Optional[bytes]=...,
        optStructVal: _typing.Optional[MyData]=...,
        optListVal: _typing.Optional[_typing.Sequence[int]]=...,
        optSetVal: _typing.Optional[_typing.AbstractSet[str]]=...,
        optMapVal: _typing.Optional[_typing.Mapping[str, str]]=...,
        unionVal: _typing.Optional[MyUnion]=...
    ) -> MyStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, int, int, int, float, float, str, bytes, MyData, bool, int, int, int, int, float, float, str, bytes, MyData, _typing.Sequence[int], _typing.AbstractSet[str], _typing.Mapping[str, str], MyUnion]]]: ...
    def _to_python(self) -> MyStruct: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStruct": ...  # type: ignore


class MyDataFieldPatch(_fbthrift_python_types.Struct):
    data1: _typing.Final[apache.thrift.op.patch.thrift_types.StringPatch] = ...
    data2: _typing.Final[apache.thrift.op.patch.thrift_types.I32Patch] = ...
    def __init__(
        self, *,
        data1: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        data2: _typing.Optional[apache.thrift.op.patch.thrift_types.I32Patch]=...
    ) -> None: ...

    def __call__(
        self, *,
        data1: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        data2: _typing.Optional[apache.thrift.op.patch.thrift_types.I32Patch]=...
    ) -> MyDataFieldPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[apache.thrift.op.patch.thrift_types.StringPatch, apache.thrift.op.patch.thrift_types.I32Patch]]]: ...
    def _to_python(self) -> MyDataFieldPatch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyDataFieldPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyDataFieldPatch": ...  # type: ignore


class MyDataPatch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[MyData]] = ...
    clear: _typing.Final[bool] = ...
    patchPrior: _typing.Final[MyDataFieldPatch] = ...
    ensure: _typing.Final[MyData] = ...
    patch: _typing.Final[MyDataFieldPatch] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[MyData]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyDataFieldPatch]=...,
        ensure: _typing.Optional[MyData]=...,
        patch: _typing.Optional[MyDataFieldPatch]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[MyData]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyDataFieldPatch]=...,
        ensure: _typing.Optional[MyData]=...,
        patch: _typing.Optional[MyDataFieldPatch]=...
    ) -> MyDataPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[MyData, bool, MyDataFieldPatch, MyData, MyDataFieldPatch]]]: ...
    def _to_python(self) -> MyDataPatch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyDataPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyDataPatch": ...  # type: ignore


class InnerUnionFieldPatch(_fbthrift_python_types.Struct):
    innerOption: _typing.Final[apache.thrift.op.patch.thrift_types.BinaryPatch] = ...
    def __init__(
        self, *,
        innerOption: _typing.Optional[apache.thrift.op.patch.thrift_types.BinaryPatch]=...
    ) -> None: ...

    def __call__(
        self, *,
        innerOption: _typing.Optional[apache.thrift.op.patch.thrift_types.BinaryPatch]=...
    ) -> InnerUnionFieldPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[apache.thrift.op.patch.thrift_types.BinaryPatch]]]: ...
    def _to_python(self) -> InnerUnionFieldPatch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.InnerUnionFieldPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.InnerUnionFieldPatch": ...  # type: ignore


class InnerUnionPatch(_fbthrift_python_types.Struct):
    assign: _typing.Final[InnerUnion] = ...
    clear: _typing.Final[bool] = ...
    patchPrior: _typing.Final[InnerUnionFieldPatch] = ...
    ensure: _typing.Final[InnerUnion] = ...
    patch: _typing.Final[InnerUnionFieldPatch] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[InnerUnion]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[InnerUnionFieldPatch]=...,
        ensure: _typing.Optional[InnerUnion]=...,
        patch: _typing.Optional[InnerUnionFieldPatch]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[InnerUnion]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[InnerUnionFieldPatch]=...,
        ensure: _typing.Optional[InnerUnion]=...,
        patch: _typing.Optional[InnerUnionFieldPatch]=...
    ) -> InnerUnionPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[InnerUnion, bool, InnerUnionFieldPatch, InnerUnion, InnerUnionFieldPatch]]]: ...
    def _to_python(self) -> InnerUnionPatch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.InnerUnionPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.InnerUnionPatch": ...  # type: ignore


class MyUnionFieldPatch(_fbthrift_python_types.Struct):
    option1: _typing.Final[apache.thrift.op.patch.thrift_types.StringPatch] = ...
    option2: _typing.Final[apache.thrift.op.patch.thrift_types.I32Patch] = ...
    option3: _typing.Final[InnerUnionPatch] = ...
    def __init__(
        self, *,
        option1: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        option2: _typing.Optional[apache.thrift.op.patch.thrift_types.I32Patch]=...,
        option3: _typing.Optional[InnerUnionPatch]=...
    ) -> None: ...

    def __call__(
        self, *,
        option1: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        option2: _typing.Optional[apache.thrift.op.patch.thrift_types.I32Patch]=...,
        option3: _typing.Optional[InnerUnionPatch]=...
    ) -> MyUnionFieldPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[apache.thrift.op.patch.thrift_types.StringPatch, apache.thrift.op.patch.thrift_types.I32Patch, InnerUnionPatch]]]: ...
    def _to_python(self) -> MyUnionFieldPatch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyUnionFieldPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyUnionFieldPatch": ...  # type: ignore


class MyUnionPatch(_fbthrift_python_types.Struct):
    assign: _typing.Final[MyUnion] = ...
    clear: _typing.Final[bool] = ...
    patchPrior: _typing.Final[MyUnionFieldPatch] = ...
    ensure: _typing.Final[MyUnion] = ...
    patch: _typing.Final[MyUnionFieldPatch] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[MyUnion]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyUnionFieldPatch]=...,
        ensure: _typing.Optional[MyUnion]=...,
        patch: _typing.Optional[MyUnionFieldPatch]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[MyUnion]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyUnionFieldPatch]=...,
        ensure: _typing.Optional[MyUnion]=...,
        patch: _typing.Optional[MyUnionFieldPatch]=...
    ) -> MyUnionPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[MyUnion, bool, MyUnionFieldPatch, MyUnion, MyUnionFieldPatch]]]: ...
    def _to_python(self) -> MyUnionPatch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyUnionPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyUnionPatch": ...  # type: ignore


class MyStructFieldPatch(_fbthrift_python_types.Struct):
    boolVal: _typing.Final[apache.thrift.op.patch.thrift_types.BoolPatch] = ...
    byteVal: _typing.Final[apache.thrift.op.patch.thrift_types.BytePatch] = ...
    i16Val: _typing.Final[apache.thrift.op.patch.thrift_types.I16Patch] = ...
    i32Val: _typing.Final[apache.thrift.op.patch.thrift_types.I32Patch] = ...
    i64Val: _typing.Final[apache.thrift.op.patch.thrift_types.I64Patch] = ...
    floatVal: _typing.Final[apache.thrift.op.patch.thrift_types.FloatPatch] = ...
    doubleVal: _typing.Final[apache.thrift.op.patch.thrift_types.DoublePatch] = ...
    stringVal: _typing.Final[apache.thrift.op.patch.thrift_types.StringPatch] = ...
    binaryVal: _typing.Final[apache.thrift.op.patch.thrift_types.BinaryPatch] = ...
    structVal: _typing.Final[MyDataPatch] = ...
    optBoolVal: _typing.Final[apache.thrift.op.patch.thrift_types.BoolPatch] = ...
    optByteVal: _typing.Final[apache.thrift.op.patch.thrift_types.BytePatch] = ...
    optI16Val: _typing.Final[apache.thrift.op.patch.thrift_types.I16Patch] = ...
    optI32Val: _typing.Final[apache.thrift.op.patch.thrift_types.I32Patch] = ...
    optI64Val: _typing.Final[apache.thrift.op.patch.thrift_types.I64Patch] = ...
    optFloatVal: _typing.Final[apache.thrift.op.patch.thrift_types.FloatPatch] = ...
    optDoubleVal: _typing.Final[apache.thrift.op.patch.thrift_types.DoublePatch] = ...
    optStringVal: _typing.Final[apache.thrift.op.patch.thrift_types.StringPatch] = ...
    optBinaryVal: _typing.Final[apache.thrift.op.patch.thrift_types.BinaryPatch] = ...
    optStructVal: _typing.Final[MyDataPatch] = ...
    optListVal: _typing.Final[MyStructField21Patch] = ...
    optSetVal: _typing.Final[MyStructField22Patch] = ...
    optMapVal: _typing.Final[MyStructField23Patch] = ...
    unionVal: _typing.Final[MyUnionPatch] = ...
    def __init__(
        self, *,
        boolVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BoolPatch]=...,
        byteVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BytePatch]=...,
        i16Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I16Patch]=...,
        i32Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I32Patch]=...,
        i64Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I64Patch]=...,
        floatVal: _typing.Optional[apache.thrift.op.patch.thrift_types.FloatPatch]=...,
        doubleVal: _typing.Optional[apache.thrift.op.patch.thrift_types.DoublePatch]=...,
        stringVal: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        binaryVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BinaryPatch]=...,
        structVal: _typing.Optional[MyDataPatch]=...,
        optBoolVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BoolPatch]=...,
        optByteVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BytePatch]=...,
        optI16Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I16Patch]=...,
        optI32Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I32Patch]=...,
        optI64Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I64Patch]=...,
        optFloatVal: _typing.Optional[apache.thrift.op.patch.thrift_types.FloatPatch]=...,
        optDoubleVal: _typing.Optional[apache.thrift.op.patch.thrift_types.DoublePatch]=...,
        optStringVal: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        optBinaryVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BinaryPatch]=...,
        optStructVal: _typing.Optional[MyDataPatch]=...,
        optListVal: _typing.Optional[MyStructField21Patch]=...,
        optSetVal: _typing.Optional[MyStructField22Patch]=...,
        optMapVal: _typing.Optional[MyStructField23Patch]=...,
        unionVal: _typing.Optional[MyUnionPatch]=...
    ) -> None: ...

    def __call__(
        self, *,
        boolVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BoolPatch]=...,
        byteVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BytePatch]=...,
        i16Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I16Patch]=...,
        i32Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I32Patch]=...,
        i64Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I64Patch]=...,
        floatVal: _typing.Optional[apache.thrift.op.patch.thrift_types.FloatPatch]=...,
        doubleVal: _typing.Optional[apache.thrift.op.patch.thrift_types.DoublePatch]=...,
        stringVal: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        binaryVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BinaryPatch]=...,
        structVal: _typing.Optional[MyDataPatch]=...,
        optBoolVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BoolPatch]=...,
        optByteVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BytePatch]=...,
        optI16Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I16Patch]=...,
        optI32Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I32Patch]=...,
        optI64Val: _typing.Optional[apache.thrift.op.patch.thrift_types.I64Patch]=...,
        optFloatVal: _typing.Optional[apache.thrift.op.patch.thrift_types.FloatPatch]=...,
        optDoubleVal: _typing.Optional[apache.thrift.op.patch.thrift_types.DoublePatch]=...,
        optStringVal: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        optBinaryVal: _typing.Optional[apache.thrift.op.patch.thrift_types.BinaryPatch]=...,
        optStructVal: _typing.Optional[MyDataPatch]=...,
        optListVal: _typing.Optional[MyStructField21Patch]=...,
        optSetVal: _typing.Optional[MyStructField22Patch]=...,
        optMapVal: _typing.Optional[MyStructField23Patch]=...,
        unionVal: _typing.Optional[MyUnionPatch]=...
    ) -> MyStructFieldPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[apache.thrift.op.patch.thrift_types.BoolPatch, apache.thrift.op.patch.thrift_types.BytePatch, apache.thrift.op.patch.thrift_types.I16Patch, apache.thrift.op.patch.thrift_types.I32Patch, apache.thrift.op.patch.thrift_types.I64Patch, apache.thrift.op.patch.thrift_types.FloatPatch, apache.thrift.op.patch.thrift_types.DoublePatch, apache.thrift.op.patch.thrift_types.StringPatch, apache.thrift.op.patch.thrift_types.BinaryPatch, MyDataPatch, apache.thrift.op.patch.thrift_types.BoolPatch, apache.thrift.op.patch.thrift_types.BytePatch, apache.thrift.op.patch.thrift_types.I16Patch, apache.thrift.op.patch.thrift_types.I32Patch, apache.thrift.op.patch.thrift_types.I64Patch, apache.thrift.op.patch.thrift_types.FloatPatch, apache.thrift.op.patch.thrift_types.DoublePatch, apache.thrift.op.patch.thrift_types.StringPatch, apache.thrift.op.patch.thrift_types.BinaryPatch, MyDataPatch, MyStructField21Patch, MyStructField22Patch, MyStructField23Patch, MyUnionPatch]]]: ...
    def _to_python(self) -> MyStructFieldPatch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyStructFieldPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructFieldPatch": ...  # type: ignore


class MyStructField21Patch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[_typing.Sequence[int]]] = ...
    clear: _typing.Final[bool] = ...
    prepend: _typing.Final[_typing.Sequence[int]] = ...
    append: _typing.Final[_typing.Sequence[int]] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[_typing.Sequence[int]]=...,
        clear: _typing.Optional[bool]=...,
        prepend: _typing.Optional[_typing.Sequence[int]]=...,
        append: _typing.Optional[_typing.Sequence[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[_typing.Sequence[int]]=...,
        clear: _typing.Optional[bool]=...,
        prepend: _typing.Optional[_typing.Sequence[int]]=...,
        append: _typing.Optional[_typing.Sequence[int]]=...
    ) -> MyStructField21Patch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.Sequence[int], bool, _typing.Sequence[int], _typing.Sequence[int]]]]: ...
    def _to_python(self) -> MyStructField21Patch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyStructField21Patch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructField21Patch": ...  # type: ignore


class MyStructField22Patch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[_typing.AbstractSet[str]]] = ...
    clear: _typing.Final[bool] = ...
    remove: _typing.Final[_typing.AbstractSet[str]] = ...
    add: _typing.Final[_typing.AbstractSet[str]] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[_typing.AbstractSet[str]]=...,
        clear: _typing.Optional[bool]=...,
        remove: _typing.Optional[_typing.AbstractSet[str]]=...,
        add: _typing.Optional[_typing.AbstractSet[str]]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[_typing.AbstractSet[str]]=...,
        clear: _typing.Optional[bool]=...,
        remove: _typing.Optional[_typing.AbstractSet[str]]=...,
        add: _typing.Optional[_typing.AbstractSet[str]]=...
    ) -> MyStructField22Patch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.AbstractSet[str], bool, _typing.AbstractSet[str], _typing.AbstractSet[str]]]]: ...
    def _to_python(self) -> MyStructField22Patch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyStructField22Patch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructField22Patch": ...  # type: ignore


class MyStructField23Patch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[_typing.Mapping[str, str]]] = ...
    clear: _typing.Final[bool] = ...
    add: _typing.Final[_typing.Mapping[str, str]] = ...
    put: _typing.Final[_typing.Mapping[str, str]] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[_typing.Mapping[str, str]]=...,
        clear: _typing.Optional[bool]=...,
        add: _typing.Optional[_typing.Mapping[str, str]]=...,
        put: _typing.Optional[_typing.Mapping[str, str]]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[_typing.Mapping[str, str]]=...,
        clear: _typing.Optional[bool]=...,
        add: _typing.Optional[_typing.Mapping[str, str]]=...,
        put: _typing.Optional[_typing.Mapping[str, str]]=...
    ) -> MyStructField23Patch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.Mapping[str, str], bool, _typing.Mapping[str, str], _typing.Mapping[str, str]]]]: ...
    def _to_python(self) -> MyStructField23Patch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyStructField23Patch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructField23Patch": ...  # type: ignore


class MyStructPatch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[MyStruct]] = ...
    clear: _typing.Final[bool] = ...
    patchPrior: _typing.Final[MyStructFieldPatch] = ...
    ensure: _typing.Final[MyStruct] = ...
    patch: _typing.Final[MyStructFieldPatch] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[MyStruct]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyStructFieldPatch]=...,
        ensure: _typing.Optional[MyStruct]=...,
        patch: _typing.Optional[MyStructFieldPatch]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[MyStruct]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyStructFieldPatch]=...,
        ensure: _typing.Optional[MyStruct]=...,
        patch: _typing.Optional[MyStructFieldPatch]=...
    ) -> MyStructPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[MyStruct, bool, MyStructFieldPatch, MyStruct, MyStructFieldPatch]]]: ...
    def _to_python(self) -> MyStructPatch: ...
    def _to_py3(self) -> "test.fixtures.patch.module.types.MyStructPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructPatch": ...  # type: ignore
