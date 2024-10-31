// Autogenerated by Thrift for thrift/compiler/test/fixtures/interactions/src/module.thrift
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//  @generated

package module


import (
    "reflect"
    "sync"

    shared "shared"
    thrift "github.com/facebook/fbthrift/thrift/lib/go/thrift/types"
)

var _ = shared.GoUnusedProtection__
// (needed to ensure safety because of naive import list construction)
var _ = thrift.ZERO
var _ = reflect.Ptr

// Premade codec specs
var (
    premadeCodecTypeSpec_string *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_CustomException *thrift.TypeSpec = nil
    premadeCodecTypeSpec_void *thrift.TypeSpec = nil
)

// Premade codec specs initializer
var premadeCodecSpecsInitOnce = sync.OnceFunc(func() {
    premadeCodecTypeSpec_string = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_STRING,
},

    }
    premadeCodecTypeSpec_module_CustomException = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewCustomException() },
},

    }
    premadeCodecTypeSpec_void = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_VOID,
},

    }
})

// Premade struct specs
var (
    premadeStructSpec_CustomException *thrift.StructSpec = nil
    premadeStructSpec_reqMyServiceFoo *thrift.StructSpec = nil
    premadeStructSpec_respMyServiceFoo *thrift.StructSpec = nil
    premadeStructSpec_reqFactoriesFoo *thrift.StructSpec = nil
    premadeStructSpec_respFactoriesFoo *thrift.StructSpec = nil
    premadeStructSpec_reqPerformFoo *thrift.StructSpec = nil
    premadeStructSpec_respPerformFoo *thrift.StructSpec = nil
    premadeStructSpec_reqInteractWithSharedDoSomeSimilarThings *thrift.StructSpec = nil
    premadeStructSpec_respInteractWithSharedDoSomeSimilarThings *thrift.StructSpec = nil
)

// Premade struct specs initializer
var premadeStructSpecsInitOnce = sync.OnceFunc(func() {
    premadeStructSpec_CustomException = &thrift.StructSpec{
    Name:               "CustomException",
    IsUnion:            false,
    IsException:        true,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "message",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
    },
}
    premadeStructSpec_reqMyServiceFoo = &thrift.StructSpec{
    Name:               "reqMyServiceFoo",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
    },
    FieldSpecIDToIndex: map[int16]int{
    },
}
    premadeStructSpec_respMyServiceFoo = &thrift.StructSpec{
    Name:               "respMyServiceFoo",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
    },
    FieldSpecIDToIndex: map[int16]int{
    },
}
    premadeStructSpec_reqFactoriesFoo = &thrift.StructSpec{
    Name:               "reqFactoriesFoo",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
    },
    FieldSpecIDToIndex: map[int16]int{
    },
}
    premadeStructSpec_respFactoriesFoo = &thrift.StructSpec{
    Name:               "respFactoriesFoo",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
    },
    FieldSpecIDToIndex: map[int16]int{
    },
}
    premadeStructSpec_reqPerformFoo = &thrift.StructSpec{
    Name:               "reqPerformFoo",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
    },
    FieldSpecIDToIndex: map[int16]int{
    },
}
    premadeStructSpec_respPerformFoo = &thrift.StructSpec{
    Name:               "respPerformFoo",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
    },
    FieldSpecIDToIndex: map[int16]int{
    },
}
    premadeStructSpec_reqInteractWithSharedDoSomeSimilarThings = &thrift.StructSpec{
    Name:               "reqInteractWithSharedDoSomeSimilarThings",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
    },
    FieldSpecIDToIndex: map[int16]int{
    },
}
    premadeStructSpec_respInteractWithSharedDoSomeSimilarThings = &thrift.StructSpec{
    Name:               "respInteractWithSharedDoSomeSimilarThings",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   0,
            WireType:             thrift.Type(thrift.STRUCT),
            Name:                 "success",
            ReflectIndex:         0,
            IsOptional:           true,
            ValueTypeSpec:        shared.GetCodecTypeSpec("shared.DoSomethingResult"),
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        0: 0,
    },
}
})

var premadeCodecSpecsMapOnce = sync.OnceValue(
    func() map[string]*thrift.TypeSpec {
        // Relies on premade codec specs initialization
        premadeCodecSpecsInitOnce()
        return map[string]*thrift.TypeSpec{
            "string": premadeCodecTypeSpec_string,
            "module.CustomException": premadeCodecTypeSpec_module_CustomException,
            "void": premadeCodecTypeSpec_void,
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
