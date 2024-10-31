// Autogenerated by Thrift for thrift/annotation/hack.thrift
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//  @generated

package hack


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
    premadeCodecTypeSpec_string *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_FieldWrapper *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_Wrapper *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_Adapter *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_SkipCodegen *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_Name *thrift.TypeSpec = nil
    premadeCodecTypeSpec_list_string *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_UnionEnumAttributes *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_StructTrait *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_Attributes *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_StructAsTrait *thrift.TypeSpec = nil
    premadeCodecTypeSpec_hack_ModuleInternal *thrift.TypeSpec = nil
)

// Premade codec specs initializer
var premadeCodecSpecsInitOnce = sync.OnceFunc(func() {
    premadeCodecTypeSpec_string = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_STRING,
},

    }
    premadeCodecTypeSpec_hack_FieldWrapper = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewFieldWrapper() },
},

    }
    premadeCodecTypeSpec_hack_Wrapper = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewWrapper() },
},

    }
    premadeCodecTypeSpec_hack_Adapter = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewAdapter() },
},

    }
    premadeCodecTypeSpec_hack_SkipCodegen = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewSkipCodegen() },
},

    }
    premadeCodecTypeSpec_hack_Name = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewName() },
},

    }
    premadeCodecTypeSpec_list_string = &thrift.TypeSpec{
        CodecListSpec: &thrift.CodecListSpec{
    ElementWireType: thrift.STRING,
	ElementTypeSpec: premadeCodecTypeSpec_string,
},

    }
    premadeCodecTypeSpec_hack_UnionEnumAttributes = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewUnionEnumAttributes() },
},

    }
    premadeCodecTypeSpec_hack_StructTrait = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewStructTrait() },
},

    }
    premadeCodecTypeSpec_hack_Attributes = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewAttributes() },
},

    }
    premadeCodecTypeSpec_hack_StructAsTrait = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewStructAsTrait() },
},

    }
    premadeCodecTypeSpec_hack_ModuleInternal = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewModuleInternal() },
},

    }
})

// Premade struct specs
var (
    premadeStructSpec_FieldWrapper *thrift.StructSpec = nil
    premadeStructSpec_Wrapper *thrift.StructSpec = nil
    premadeStructSpec_Adapter *thrift.StructSpec = nil
    premadeStructSpec_SkipCodegen *thrift.StructSpec = nil
    premadeStructSpec_Name *thrift.StructSpec = nil
    premadeStructSpec_UnionEnumAttributes *thrift.StructSpec = nil
    premadeStructSpec_StructTrait *thrift.StructSpec = nil
    premadeStructSpec_Attributes *thrift.StructSpec = nil
    premadeStructSpec_StructAsTrait *thrift.StructSpec = nil
    premadeStructSpec_ModuleInternal *thrift.StructSpec = nil
)

// Premade struct specs initializer
var premadeStructSpecsInitOnce = sync.OnceFunc(func() {
    premadeStructSpec_FieldWrapper = &thrift.StructSpec{
    Name:               "FieldWrapper",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "name",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
    },
}
    premadeStructSpec_Wrapper = &thrift.StructSpec{
    Name:               "Wrapper",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "name",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },        {
            ID:                   2,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "underlyingName",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },        {
            ID:                   3,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "extraNamespace",
            ReflectIndex:         2,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
        2: 1,
        3: 2,
    },
}
    premadeStructSpec_Adapter = &thrift.StructSpec{
    Name:               "Adapter",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "name",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
    },
}
    premadeStructSpec_SkipCodegen = &thrift.StructSpec{
    Name:               "SkipCodegen",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "reason",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
    },
}
    premadeStructSpec_Name = &thrift.StructSpec{
    Name:               "Name",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "name",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },        {
            ID:                   2,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "reason",
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
    premadeStructSpec_UnionEnumAttributes = &thrift.StructSpec{
    Name:               "UnionEnumAttributes",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.LIST),
            Name:                 "attributes",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_list_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
    },
}
    premadeStructSpec_StructTrait = &thrift.StructSpec{
    Name:               "StructTrait",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "name",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
    },
}
    premadeStructSpec_Attributes = &thrift.StructSpec{
    Name:               "Attributes",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.LIST),
            Name:                 "attributes",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_list_string,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
    },
}
    premadeStructSpec_StructAsTrait = &thrift.StructSpec{
    Name:               "StructAsTrait",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
    },
    FieldSpecIDToIndex: map[int16]int{
    },
}
    premadeStructSpec_ModuleInternal = &thrift.StructSpec{
    Name:               "ModuleInternal",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
    },
    FieldSpecIDToIndex: map[int16]int{
    },
}
})

var premadeCodecSpecsMapOnce = sync.OnceValue(
    func() map[string]*thrift.TypeSpec {
        // Relies on premade codec specs initialization
        premadeCodecSpecsInitOnce()
        return map[string]*thrift.TypeSpec{
            "string": premadeCodecTypeSpec_string,
            "hack.FieldWrapper": premadeCodecTypeSpec_hack_FieldWrapper,
            "hack.Wrapper": premadeCodecTypeSpec_hack_Wrapper,
            "hack.Adapter": premadeCodecTypeSpec_hack_Adapter,
            "hack.SkipCodegen": premadeCodecTypeSpec_hack_SkipCodegen,
            "hack.Name": premadeCodecTypeSpec_hack_Name,
            "hack.UnionEnumAttributes": premadeCodecTypeSpec_hack_UnionEnumAttributes,
            "hack.StructTrait": premadeCodecTypeSpec_hack_StructTrait,
            "hack.Attributes": premadeCodecTypeSpec_hack_Attributes,
            "hack.StructAsTrait": premadeCodecTypeSpec_hack_StructAsTrait,
            "hack.ModuleInternal": premadeCodecTypeSpec_hack_ModuleInternal,
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
