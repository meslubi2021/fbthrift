// Autogenerated by Thrift for thrift/compiler/test/fixtures/complex-union/src/module.thrift
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//  @generated

package module


import (
    "reflect"
    "sync"

    thrift "github.com/facebook/fbthrift/thrift/lib/go/thrift/types"
)

// (needed to ensure safety because of naive import list construction)
var _ = thrift.ZERO
var _ = reflect.Ptr

// Premade codec specs
var (
    premadeCodecTypeSpec_i64 *thrift.TypeSpec = nil
    premadeCodecTypeSpec_string *thrift.TypeSpec = nil
    premadeCodecTypeSpec_list_i64 *thrift.TypeSpec = nil
    premadeCodecTypeSpec_list_string *thrift.TypeSpec = nil
    premadeCodecTypeSpec_i16 *thrift.TypeSpec = nil
    premadeCodecTypeSpec_map_i16_string *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_containerTypedef *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_ComplexUnion *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_ListUnion *thrift.TypeSpec = nil
    premadeCodecTypeSpec_binary *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_DataUnion *thrift.TypeSpec = nil
    premadeCodecTypeSpec_i32 *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_Val *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_ValUnion *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_VirtualComplexUnion *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_NonCopyableStruct *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_NonCopyableUnion *thrift.TypeSpec = nil
)

// Premade codec specs initializer
var premadeCodecSpecsInitOnce = sync.OnceFunc(func() {
    premadeCodecTypeSpec_i64 = &thrift.TypeSpec{
        FullName: "i64",
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_I64,
},

    }
    premadeCodecTypeSpec_string = &thrift.TypeSpec{
        FullName: "string",
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_STRING,
},

    }
    premadeCodecTypeSpec_list_i64 = &thrift.TypeSpec{
        FullName: "list<i64>",
        CodecListSpec: &thrift.CodecListSpec{
    ElementWireType: thrift.I64,
	ElementTypeSpec: premadeCodecTypeSpec_i64,
},

    }
    premadeCodecTypeSpec_list_string = &thrift.TypeSpec{
        FullName: "list<string>",
        CodecListSpec: &thrift.CodecListSpec{
    ElementWireType: thrift.STRING,
	ElementTypeSpec: premadeCodecTypeSpec_string,
},

    }
    premadeCodecTypeSpec_i16 = &thrift.TypeSpec{
        FullName: "i16",
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_I16,
},

    }
    premadeCodecTypeSpec_map_i16_string = &thrift.TypeSpec{
        FullName: "map<i16, string>",
        CodecMapSpec: &thrift.CodecMapSpec{
	KeyTypeSpec:   premadeCodecTypeSpec_i16,
	ValueTypeSpec: premadeCodecTypeSpec_string,
    KeyWireType:   thrift.I16,
	ValueWireType: thrift.STRING,
},

    }
    premadeCodecTypeSpec_module_containerTypedef = &thrift.TypeSpec{
        FullName: "module.containerTypedef",
        CodecTypedefSpec: &thrift.CodecTypedefSpec{
    ScopedName:         "module.containerTypedef",
	UnderlyingTypeSpec: premadeCodecTypeSpec_map_i16_string,
},

    }
    premadeCodecTypeSpec_module_ComplexUnion = &thrift.TypeSpec{
        FullName: "module.ComplexUnion",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.ComplexUnion",
    IsUnion:    true,
    NewFunc:    func() thrift.Struct { return NewComplexUnion() },
},

    }
    premadeCodecTypeSpec_module_ListUnion = &thrift.TypeSpec{
        FullName: "module.ListUnion",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.ListUnion",
    IsUnion:    true,
    NewFunc:    func() thrift.Struct { return NewListUnion() },
},

    }
    premadeCodecTypeSpec_binary = &thrift.TypeSpec{
        FullName: "binary",
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_BINARY,
},

    }
    premadeCodecTypeSpec_module_DataUnion = &thrift.TypeSpec{
        FullName: "module.DataUnion",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.DataUnion",
    IsUnion:    true,
    NewFunc:    func() thrift.Struct { return NewDataUnion() },
},

    }
    premadeCodecTypeSpec_i32 = &thrift.TypeSpec{
        FullName: "i32",
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_I32,
},

    }
    premadeCodecTypeSpec_module_Val = &thrift.TypeSpec{
        FullName: "module.Val",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.Val",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewVal() },
},

    }
    premadeCodecTypeSpec_module_ValUnion = &thrift.TypeSpec{
        FullName: "module.ValUnion",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.ValUnion",
    IsUnion:    true,
    NewFunc:    func() thrift.Struct { return NewValUnion() },
},

    }
    premadeCodecTypeSpec_module_VirtualComplexUnion = &thrift.TypeSpec{
        FullName: "module.VirtualComplexUnion",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.VirtualComplexUnion",
    IsUnion:    true,
    NewFunc:    func() thrift.Struct { return NewVirtualComplexUnion() },
},

    }
    premadeCodecTypeSpec_module_NonCopyableStruct = &thrift.TypeSpec{
        FullName: "module.NonCopyableStruct",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.NonCopyableStruct",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewNonCopyableStruct() },
},

    }
    premadeCodecTypeSpec_module_NonCopyableUnion = &thrift.TypeSpec{
        FullName: "module.NonCopyableUnion",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.NonCopyableUnion",
    IsUnion:    true,
    NewFunc:    func() thrift.Struct { return NewNonCopyableUnion() },
},

    }
})

// Premade struct specs
var (
    premadeStructSpec_ComplexUnion *thrift.StructSpec = nil
    premadeStructSpec_ListUnion *thrift.StructSpec = nil
    premadeStructSpec_DataUnion *thrift.StructSpec = nil
    premadeStructSpec_Val *thrift.StructSpec = nil
    premadeStructSpec_ValUnion *thrift.StructSpec = nil
    premadeStructSpec_VirtualComplexUnion *thrift.StructSpec = nil
    premadeStructSpec_NonCopyableStruct *thrift.StructSpec = nil
    premadeStructSpec_NonCopyableUnion *thrift.StructSpec = nil
)

// Premade struct specs initializer
var premadeStructSpecsInitOnce = sync.OnceFunc(func() {
    premadeStructSpec_ComplexUnion = &thrift.StructSpec{
    Name:                 "ComplexUnion",
    ScopedName:           "module.ComplexUnion",
    IsUnion:              true,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.I64,
            Name:                 "intValue",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i64,
            MustBeSetToSerialize: true,
        },        {
            ID:                   2,
            WireType:             thrift.LIST,
            Name:                 "intListValue",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_list_i64,
            MustBeSetToSerialize: true,
        },        {
            ID:                   3,
            WireType:             thrift.LIST,
            Name:                 "stringListValue",
            ReflectIndex:         2,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_list_string,
            MustBeSetToSerialize: true,
        },        {
            ID:                   5,
            WireType:             thrift.STRING,
            Name:                 "stringValue",
            ReflectIndex:         3,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: true,
        },        {
            ID:                   9,
            WireType:             thrift.MAP,
            Name:                 "typedefValue",
            ReflectIndex:         4,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_containerTypedef,
            MustBeSetToSerialize: true,
        },        {
            ID:                   14,
            WireType:             thrift.STRING,
            Name:                 "stringRef",
            ReflectIndex:         5,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
        2: 1,
        3: 2,
        5: 3,
        9: 4,
        14: 5,
    },
    FieldSpecNameToIndex: map[string]int{
        "intValue": 0,
        "intListValue": 1,
        "stringListValue": 2,
        "stringValue": 3,
        "typedefValue": 4,
        "stringRef": 5,
    },
}
    premadeStructSpec_ListUnion = &thrift.StructSpec{
    Name:                 "ListUnion",
    ScopedName:           "module.ListUnion",
    IsUnion:              true,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   2,
            WireType:             thrift.LIST,
            Name:                 "intListValue",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_list_i64,
            MustBeSetToSerialize: true,
        },        {
            ID:                   3,
            WireType:             thrift.LIST,
            Name:                 "stringListValue",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_list_string,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        2: 0,
        3: 1,
    },
    FieldSpecNameToIndex: map[string]int{
        "intListValue": 0,
        "stringListValue": 1,
    },
}
    premadeStructSpec_DataUnion = &thrift.StructSpec{
    Name:                 "DataUnion",
    ScopedName:           "module.DataUnion",
    IsUnion:              true,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.STRING,
            Name:                 "binaryData",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_binary,
            MustBeSetToSerialize: true,
        },        {
            ID:                   2,
            WireType:             thrift.STRING,
            Name:                 "stringData",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
        2: 1,
    },
    FieldSpecNameToIndex: map[string]int{
        "binaryData": 0,
        "stringData": 1,
    },
}
    premadeStructSpec_Val = &thrift.StructSpec{
    Name:                 "Val",
    ScopedName:           "module.Val",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.STRING,
            Name:                 "strVal",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },        {
            ID:                   2,
            WireType:             thrift.I32,
            Name:                 "intVal",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: false,
        },        {
            ID:                   9,
            WireType:             thrift.MAP,
            Name:                 "typedefValue",
            ReflectIndex:         2,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_containerTypedef,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
        2: 1,
        9: 2,
    },
    FieldSpecNameToIndex: map[string]int{
        "strVal": 0,
        "intVal": 1,
        "typedefValue": 2,
    },
}
    premadeStructSpec_ValUnion = &thrift.StructSpec{
    Name:                 "ValUnion",
    ScopedName:           "module.ValUnion",
    IsUnion:              true,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.STRUCT,
            Name:                 "v1",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_Val,
            MustBeSetToSerialize: true,
        },        {
            ID:                   2,
            WireType:             thrift.STRUCT,
            Name:                 "v2",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_Val,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
        2: 1,
    },
    FieldSpecNameToIndex: map[string]int{
        "v1": 0,
        "v2": 1,
    },
}
    premadeStructSpec_VirtualComplexUnion = &thrift.StructSpec{
    Name:                 "VirtualComplexUnion",
    ScopedName:           "module.VirtualComplexUnion",
    IsUnion:              true,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.STRING,
            Name:                 "thingOne",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: true,
        },        {
            ID:                   2,
            WireType:             thrift.STRING,
            Name:                 "thingTwo",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
        2: 1,
    },
    FieldSpecNameToIndex: map[string]int{
        "thingOne": 0,
        "thingTwo": 1,
    },
}
    premadeStructSpec_NonCopyableStruct = &thrift.StructSpec{
    Name:                 "NonCopyableStruct",
    ScopedName:           "module.NonCopyableStruct",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.I64,
            Name:                 "num",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i64,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
    },
    FieldSpecNameToIndex: map[string]int{
        "num": 0,
    },
}
    premadeStructSpec_NonCopyableUnion = &thrift.StructSpec{
    Name:                 "NonCopyableUnion",
    ScopedName:           "module.NonCopyableUnion",
    IsUnion:              true,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.STRUCT,
            Name:                 "s",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_NonCopyableStruct,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
    },
    FieldSpecNameToIndex: map[string]int{
        "s": 0,
    },
}
})

// Premade slice of all struct specs
var premadeStructSpecsOnce = sync.OnceValue(
    func() []*thrift.StructSpec {
        // Relies on premade struct specs
        premadeStructSpecsInitOnce()

        fbthriftResults := make([]*thrift.StructSpec, 0)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_ComplexUnion)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_ListUnion)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_DataUnion)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Val)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_ValUnion)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_VirtualComplexUnion)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_NonCopyableStruct)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_NonCopyableUnion)
        return fbthriftResults
    },
)

var premadeCodecSpecsMapOnce = sync.OnceValue(
    func() map[string]*thrift.TypeSpec {
        // Relies on premade codec specs initialization
        premadeCodecSpecsInitOnce()

        fbthriftTypeSpecsMap := make(map[string]*thrift.TypeSpec)
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_i64.FullName] = premadeCodecTypeSpec_i64
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_string.FullName] = premadeCodecTypeSpec_string
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_i16.FullName] = premadeCodecTypeSpec_i16
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_containerTypedef.FullName] = premadeCodecTypeSpec_module_containerTypedef
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_ComplexUnion.FullName] = premadeCodecTypeSpec_module_ComplexUnion
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_ListUnion.FullName] = premadeCodecTypeSpec_module_ListUnion
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_binary.FullName] = premadeCodecTypeSpec_binary
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_DataUnion.FullName] = premadeCodecTypeSpec_module_DataUnion
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_i32.FullName] = premadeCodecTypeSpec_i32
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_Val.FullName] = premadeCodecTypeSpec_module_Val
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_ValUnion.FullName] = premadeCodecTypeSpec_module_ValUnion
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_VirtualComplexUnion.FullName] = premadeCodecTypeSpec_module_VirtualComplexUnion
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_NonCopyableStruct.FullName] = premadeCodecTypeSpec_module_NonCopyableStruct
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_NonCopyableUnion.FullName] = premadeCodecTypeSpec_module_NonCopyableUnion
        return fbthriftTypeSpecsMap
    },
)

func init() {
    premadeCodecSpecsInitOnce()
    premadeStructSpecsInitOnce()
}

// GetMetadataThriftType (INTERNAL USE ONLY).
// Returns metadata TypeSpec for a given full type name.
func GetCodecTypeSpec(fullName string) *thrift.TypeSpec {
    return premadeCodecSpecsMapOnce()[fullName]
}
