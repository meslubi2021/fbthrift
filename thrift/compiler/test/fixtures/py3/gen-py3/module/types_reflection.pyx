#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#


import folly.iobuf as _fbthrift_iobuf

from thrift.py3.reflection cimport (
    NumberType as __NumberType,
    StructType as __StructType,
    Qualifier as __Qualifier,
)


cimport module.types as _module_types

from thrift.py3.types cimport (
    constant_shared_ptr,
    default_inst,
)


cdef __StructSpec get_reflection__SimpleException():
    cdef _module_types.SimpleException defaults = _module_types.SimpleException.create(
        constant_shared_ptr[_module_types.cSimpleException](
            default_inst[_module_types.cSimpleException]()
        )
    )
    cdef __StructSpec spec = __StructSpec.create(
        name="SimpleException",
        kind=__StructType.EXCEPTION,
        annotations={
        },
    )
    spec.add_field(
        __FieldSpec.create(
            id=1,
            name="err_code",
            type=int,
            kind=__NumberType.I16,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    return spec
cdef __StructSpec get_reflection__OptionalRefStruct():
    cdef _module_types.OptionalRefStruct defaults = _module_types.OptionalRefStruct.create(
        constant_shared_ptr[_module_types.cOptionalRefStruct](
            default_inst[_module_types.cOptionalRefStruct]()
        )
    )
    cdef __StructSpec spec = __StructSpec.create(
        name="OptionalRefStruct",
        kind=__StructType.STRUCT,
        annotations={
        },
    )
    spec.add_field(
        __FieldSpec.create(
            id=1,
            name="optional_blob",
            type=_fbthrift_iobuf.IOBuf,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.OPTIONAL,
            default=None,
            annotations={
            },
        ),
    )
    return spec
cdef __StructSpec get_reflection__SimpleStruct():
    cdef _module_types.SimpleStruct defaults = _module_types.SimpleStruct.create(
        constant_shared_ptr[_module_types.cSimpleStruct](
            default_inst[_module_types.cSimpleStruct]()
        )
    )
    cdef __StructSpec spec = __StructSpec.create(
        name="SimpleStruct",
        kind=__StructType.STRUCT,
        annotations={
        },
    )
    spec.add_field(
        __FieldSpec.create(
            id=1,
            name="is_on",
            type=bool,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=2,
            name="tiny_int",
            type=int,
            kind=__NumberType.BYTE,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=3,
            name="small_int",
            type=int,
            kind=__NumberType.I16,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=4,
            name="nice_sized_int",
            type=int,
            kind=__NumberType.I32,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=5,
            name="big_int",
            type=int,
            kind=__NumberType.I64,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=6,
            name="real",
            type=float,
            kind=__NumberType.DOUBLE,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=7,
            name="smaller_real",
            type=float,
            kind=__NumberType.FLOAT,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    return spec
cdef __StructSpec get_reflection__ComplexStruct():
    cdef _module_types.ComplexStruct defaults = _module_types.ComplexStruct.create(
        constant_shared_ptr[_module_types.cComplexStruct](
            default_inst[_module_types.cComplexStruct]()
        )
    )
    cdef __StructSpec spec = __StructSpec.create(
        name="ComplexStruct",
        kind=__StructType.STRUCT,
        annotations={
        },
    )
    spec.add_field(
        __FieldSpec.create(
            id=1,
            name="structOne",
            type=_module_types.SimpleStruct,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=2,
            name="structTwo",
            type=_module_types.SimpleStruct,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=3,
            name="an_integer",
            type=int,
            kind=__NumberType.I32,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=4,
            name="name",
            type=str,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=5,
            name="an_enum",
            type=_module_types.AnEnum,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=6,
            name="some_bytes",
            type=bytes,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=7,
            name="from",
            type=str,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
                """py3.name""": """sender""",            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=8,
            name="cdef",
            type=str,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    spec.add_field(
        __FieldSpec.create(
            id=9,
            name="bytes_with_cpp_type",
            type=bytes,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    return spec
cdef __StructSpec get_reflection__BinaryUnion():
    cdef __StructSpec spec = __StructSpec.create(
        name="BinaryUnion",
        kind=__StructType.UNION,
        annotations={
            """cpp.noncomparable""": """1""",        },
    )
    spec.add_field(
        __FieldSpec.create(
            id=1,
            name="iobuf_val",
            type=_fbthrift_iobuf.IOBuf,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    return spec
cdef __StructSpec get_reflection__BinaryUnionStruct():
    cdef _module_types.BinaryUnionStruct defaults = _module_types.BinaryUnionStruct.create(
        constant_shared_ptr[_module_types.cBinaryUnionStruct](
            default_inst[_module_types.cBinaryUnionStruct]()
        )
    )
    cdef __StructSpec spec = __StructSpec.create(
        name="BinaryUnionStruct",
        kind=__StructType.STRUCT,
        annotations={
            """cpp.noncomparable""": """1""",        },
    )
    spec.add_field(
        __FieldSpec.create(
            id=1,
            name="u",
            type=_module_types.BinaryUnion,
            kind=__NumberType.NOT_A_NUMBER,
            qualifier=__Qualifier.UNQUALIFIED,
            default=None,
            annotations={
            },
        ),
    )
    return spec
cdef __ListSpec get_reflection__List__i16():
    return __ListSpec.create(
        value=int,
        kind=__NumberType.I16,
    )

cdef __ListSpec get_reflection__List__i32():
    return __ListSpec.create(
        value=int,
        kind=__NumberType.I32,
    )

cdef __ListSpec get_reflection__List__i64():
    return __ListSpec.create(
        value=int,
        kind=__NumberType.I64,
    )

cdef __ListSpec get_reflection__List__string():
    return __ListSpec.create(
        value=str,
        kind=__NumberType.NOT_A_NUMBER,
    )

cdef __ListSpec get_reflection__List__SimpleStruct():
    return __ListSpec.create(
        value=_module_types.SimpleStruct,
        kind=__NumberType.NOT_A_NUMBER,
    )

cdef __SetSpec get_reflection__Set__i32():
    return __SetSpec.create(
        value=int,
        kind=__NumberType.I32,
     )

cdef __SetSpec get_reflection__Set__string():
    return __SetSpec.create(
        value=str,
        kind=__NumberType.NOT_A_NUMBER,
     )

cdef __MapSpec get_reflection__Map__string_string():
    return __MapSpec.create(
        key=str,
        key_kind=__NumberType.NOT_A_NUMBER,
        value=str,
        value_kind=__NumberType.NOT_A_NUMBER,
    )

cdef __MapSpec get_reflection__Map__string_SimpleStruct():
    return __MapSpec.create(
        key=str,
        key_kind=__NumberType.NOT_A_NUMBER,
        value=_module_types.SimpleStruct,
        value_kind=__NumberType.NOT_A_NUMBER,
    )

cdef __MapSpec get_reflection__Map__string_i16():
    return __MapSpec.create(
        key=str,
        key_kind=__NumberType.NOT_A_NUMBER,
        value=int,
        value_kind=__NumberType.I16,
    )

cdef __ListSpec get_reflection__List__List__i32():
    return __ListSpec.create(
        value=_module_types.List__i32,
        kind=__NumberType.NOT_A_NUMBER,
    )

cdef __MapSpec get_reflection__Map__string_i32():
    return __MapSpec.create(
        key=str,
        key_kind=__NumberType.NOT_A_NUMBER,
        value=int,
        value_kind=__NumberType.I32,
    )

cdef __MapSpec get_reflection__Map__string_Map__string_i32():
    return __MapSpec.create(
        key=str,
        key_kind=__NumberType.NOT_A_NUMBER,
        value=_module_types.Map__string_i32,
        value_kind=__NumberType.NOT_A_NUMBER,
    )

cdef __ListSpec get_reflection__List__Set__string():
    return __ListSpec.create(
        value=_module_types.Set__string,
        kind=__NumberType.NOT_A_NUMBER,
    )

cdef __MapSpec get_reflection__Map__string_List__SimpleStruct():
    return __MapSpec.create(
        key=str,
        key_kind=__NumberType.NOT_A_NUMBER,
        value=_module_types.List__SimpleStruct,
        value_kind=__NumberType.NOT_A_NUMBER,
    )

cdef __ListSpec get_reflection__List__List__string():
    return __ListSpec.create(
        value=_module_types.List__string,
        kind=__NumberType.NOT_A_NUMBER,
    )

cdef __ListSpec get_reflection__List__Set__i32():
    return __ListSpec.create(
        value=_module_types.Set__i32,
        kind=__NumberType.NOT_A_NUMBER,
    )

cdef __ListSpec get_reflection__List__Map__string_string():
    return __ListSpec.create(
        value=_module_types.Map__string_string,
        kind=__NumberType.NOT_A_NUMBER,
    )

cdef __ListSpec get_reflection__List__binary():
    return __ListSpec.create(
        value=bytes,
        kind=__NumberType.NOT_A_NUMBER,
    )

cdef __SetSpec get_reflection__Set__binary():
    return __SetSpec.create(
        value=bytes,
        kind=__NumberType.NOT_A_NUMBER,
     )

cdef __ListSpec get_reflection__List__AnEnum():
    return __ListSpec.create(
        value=_module_types.AnEnum,
        kind=__NumberType.NOT_A_NUMBER,
    )

cdef __MapSpec get_reflection__Map__i32_double():
    return __MapSpec.create(
        key=int,
        key_kind=__NumberType.I32,
        value=float,
        value_kind=__NumberType.DOUBLE,
    )

cdef __ListSpec get_reflection__List__Map__i32_double():
    return __ListSpec.create(
        value=_module_types.Map__i32_double,
        kind=__NumberType.NOT_A_NUMBER,
    )

