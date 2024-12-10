// Autogenerated by Thrift for thrift/compiler/test/fixtures/default_values/src/module.thrift
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
    premadeCodecTypeSpec_i32 *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_TrivialStruct *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_StructWithNoCustomDefaultValues *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_StructWithCustomDefaultValues *thrift.TypeSpec = nil
)

// Premade codec specs initializer
var premadeCodecSpecsInitOnce = sync.OnceFunc(func() {
    premadeCodecTypeSpec_i32 = &thrift.TypeSpec{
        FullName: "i32",
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_I32,
},

    }
    premadeCodecTypeSpec_module_TrivialStruct = &thrift.TypeSpec{
        FullName: "module.TrivialStruct",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.TrivialStruct",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewTrivialStruct() },
},

    }
    premadeCodecTypeSpec_module_StructWithNoCustomDefaultValues = &thrift.TypeSpec{
        FullName: "module.StructWithNoCustomDefaultValues",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.StructWithNoCustomDefaultValues",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewStructWithNoCustomDefaultValues() },
},

    }
    premadeCodecTypeSpec_module_StructWithCustomDefaultValues = &thrift.TypeSpec{
        FullName: "module.StructWithCustomDefaultValues",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "module.StructWithCustomDefaultValues",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewStructWithCustomDefaultValues() },
},

    }
})

// Premade struct specs
var (
    premadeStructSpec_TrivialStruct *thrift.StructSpec = nil
    premadeStructSpec_StructWithNoCustomDefaultValues *thrift.StructSpec = nil
    premadeStructSpec_StructWithCustomDefaultValues *thrift.StructSpec = nil
)

// Premade struct specs initializer
var premadeStructSpecsInitOnce = sync.OnceFunc(func() {
    premadeStructSpec_TrivialStruct = &thrift.StructSpec{
    Name:                 "TrivialStruct",
    ScopedName:           "module.TrivialStruct",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.I32,
            Name:                 "int_value",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
    },
    FieldSpecNameToIndex: map[string]int{
        "int_value": 0,
    },
}
    premadeStructSpec_StructWithNoCustomDefaultValues = &thrift.StructSpec{
    Name:                 "StructWithNoCustomDefaultValues",
    ScopedName:           "module.StructWithNoCustomDefaultValues",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.I32,
            Name:                 "unqualified_integer",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: false,
        },        {
            ID:                   2,
            WireType:             thrift.I32,
            Name:                 "optional_integer",
            ReflectIndex:         1,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: true,
        },        {
            ID:                   3,
            WireType:             thrift.I32,
            Name:                 "required_integer",
            ReflectIndex:         2,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: false,
        },        {
            ID:                   4,
            WireType:             thrift.STRUCT,
            Name:                 "unqualified_struct",
            ReflectIndex:         3,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_TrivialStruct,
            MustBeSetToSerialize: true,
        },        {
            ID:                   5,
            WireType:             thrift.STRUCT,
            Name:                 "optional_struct",
            ReflectIndex:         4,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_module_TrivialStruct,
            MustBeSetToSerialize: true,
        },        {
            ID:                   6,
            WireType:             thrift.STRUCT,
            Name:                 "required_struct",
            ReflectIndex:         5,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_TrivialStruct,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
    },
    FieldSpecNameToIndex: map[string]int{
        "unqualified_integer": 0,
        "optional_integer": 1,
        "required_integer": 2,
        "unqualified_struct": 3,
        "optional_struct": 4,
        "required_struct": 5,
    },
}
    premadeStructSpec_StructWithCustomDefaultValues = &thrift.StructSpec{
    Name:                 "StructWithCustomDefaultValues",
    ScopedName:           "module.StructWithCustomDefaultValues",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.I32,
            Name:                 "unqualified_integer",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: false,
        },        {
            ID:                   2,
            WireType:             thrift.I32,
            Name:                 "optional_integer",
            ReflectIndex:         1,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: true,
        },        {
            ID:                   3,
            WireType:             thrift.I32,
            Name:                 "required_integer",
            ReflectIndex:         2,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: false,
        },        {
            ID:                   4,
            WireType:             thrift.STRUCT,
            Name:                 "unqualified_struct",
            ReflectIndex:         3,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_TrivialStruct,
            MustBeSetToSerialize: true,
        },        {
            ID:                   5,
            WireType:             thrift.STRUCT,
            Name:                 "optional_struct",
            ReflectIndex:         4,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_module_TrivialStruct,
            MustBeSetToSerialize: true,
        },        {
            ID:                   6,
            WireType:             thrift.STRUCT,
            Name:                 "required_struct",
            ReflectIndex:         5,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_TrivialStruct,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex:   map[int16]int{
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
    },
    FieldSpecNameToIndex: map[string]int{
        "unqualified_integer": 0,
        "optional_integer": 1,
        "required_integer": 2,
        "unqualified_struct": 3,
        "optional_struct": 4,
        "required_struct": 5,
    },
}
})

// Premade slice of all struct specs
var premadeStructSpecsOnce = sync.OnceValue(
    func() []*thrift.StructSpec {
        // Relies on premade struct specs
        premadeStructSpecsInitOnce()

        fbthriftResults := make([]*thrift.StructSpec, 0)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_TrivialStruct)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_StructWithNoCustomDefaultValues)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_StructWithCustomDefaultValues)
        return fbthriftResults
    },
)

var premadeCodecSpecsMapOnce = sync.OnceValue(
    func() map[string]*thrift.TypeSpec {
        // Relies on premade codec specs initialization
        premadeCodecSpecsInitOnce()

        fbthriftTypeSpecsMap := make(map[string]*thrift.TypeSpec)
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_i32.FullName] = premadeCodecTypeSpec_i32
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_TrivialStruct.FullName] = premadeCodecTypeSpec_module_TrivialStruct
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_StructWithNoCustomDefaultValues.FullName] = premadeCodecTypeSpec_module_StructWithNoCustomDefaultValues
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_module_StructWithCustomDefaultValues.FullName] = premadeCodecTypeSpec_module_StructWithCustomDefaultValues
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
