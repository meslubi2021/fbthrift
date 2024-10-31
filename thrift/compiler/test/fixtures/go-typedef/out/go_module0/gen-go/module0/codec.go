// Autogenerated by Thrift for thrift/compiler/test/fixtures/go-typedef/src/module0.thrift
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//  @generated

package module0


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
    premadeCodecTypeSpec_string *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module0_Accessory *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module0_PartName *thrift.TypeSpec = nil
)

// Premade codec specs initializer
var premadeCodecSpecsInitOnce = sync.OnceFunc(func() {
    premadeCodecTypeSpec_i32 = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_I32,
},

    }
    premadeCodecTypeSpec_string = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_STRING,
},

    }
    premadeCodecTypeSpec_module0_Accessory = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewAccessory() },
},

    }
    premadeCodecTypeSpec_module0_PartName = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewPartName() },
},

    }
})

// Premade struct specs
var (
    premadeStructSpec_Accessory *thrift.StructSpec = nil
    premadeStructSpec_PartName *thrift.StructSpec = nil
)

// Premade struct specs initializer
var premadeStructSpecsInitOnce = sync.OnceFunc(func() {
    premadeStructSpec_Accessory = &thrift.StructSpec{
    Name:               "Accessory",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.I32),
            Name:                 "InventoryId",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: false,
        },        {
            ID:                   2,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "Name",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
        2: 1,
    },
}
    premadeStructSpec_PartName = &thrift.StructSpec{
    Name:               "PartName",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.I32),
            Name:                 "InventoryId",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_i32,
            MustBeSetToSerialize: false,
        },        {
            ID:                   2,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "Name",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
        2: 1,
    },
}
})

var premadeCodecSpecsMapOnce = sync.OnceValue(
    func() map[string]*thrift.TypeSpec {
        // Relies on premade codec specs initialization
        premadeCodecSpecsInitOnce()
        return map[string]*thrift.TypeSpec{
            "i32": premadeCodecTypeSpec_i32,
            "string": premadeCodecTypeSpec_string,
            "module0.Accessory": premadeCodecTypeSpec_module0_Accessory,
            "module0.PartName": premadeCodecTypeSpec_module0_PartName,
        }
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
