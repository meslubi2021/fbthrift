// Autogenerated by Thrift for thrift/compiler/test/fixtures/optionals/src/module.thrift
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
    premadeCodecTypeSpec_module_Animal *thrift.TypeSpec = nil
    premadeCodecTypeSpec_double *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_Color *thrift.TypeSpec = nil
    premadeCodecTypeSpec_string *thrift.TypeSpec = nil
    premadeCodecTypeSpec_bool *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_Vehicle *thrift.TypeSpec = nil
    premadeCodecTypeSpec_i64 *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_PersonID *thrift.TypeSpec = nil
    premadeCodecTypeSpec_i16 *thrift.TypeSpec = nil
    premadeCodecTypeSpec_set_module_PersonID *thrift.TypeSpec = nil
    premadeCodecTypeSpec_map_module_Animal_string *thrift.TypeSpec = nil
    premadeCodecTypeSpec_list_module_Vehicle *thrift.TypeSpec = nil
    premadeCodecTypeSpec_module_Person *thrift.TypeSpec = nil
)

// Premade codec specs initializer
var premadeCodecSpecsInitOnce = sync.OnceFunc(func() {
    premadeCodecTypeSpec_module_Animal = &thrift.TypeSpec{
        CodecEnumSpec: &thrift.CodecEnumSpec{},

    }
    premadeCodecTypeSpec_double = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_DOUBLE,
},

    }
    premadeCodecTypeSpec_module_Color = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewColor() },
},

    }
    premadeCodecTypeSpec_string = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_STRING,
},

    }
    premadeCodecTypeSpec_bool = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_BOOL,
},

    }
    premadeCodecTypeSpec_module_Vehicle = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewVehicle() },
},

    }
    premadeCodecTypeSpec_i64 = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_I64,
},

    }
    premadeCodecTypeSpec_module_PersonID = &thrift.TypeSpec{
        CodecTypedefSpec: &thrift.CodecTypedefSpec{
	UnderlyingTypeSpec: premadeCodecTypeSpec_i64,
},

    }
    premadeCodecTypeSpec_i16 = &thrift.TypeSpec{
        CodecPrimitiveSpec: &thrift.CodecPrimitiveSpec{
    PrimitiveType: thrift.CODEC_PRIMITIVE_TYPE_I16,
},

    }
    premadeCodecTypeSpec_set_module_PersonID = &thrift.TypeSpec{
        CodecSetSpec: &thrift.CodecSetSpec{
    ElementWireType: thrift.I64,
	ElementTypeSpec: premadeCodecTypeSpec_module_PersonID,
},

    }
    premadeCodecTypeSpec_map_module_Animal_string = &thrift.TypeSpec{
        CodecMapSpec: &thrift.CodecMapSpec{
	KeyTypeSpec:   premadeCodecTypeSpec_module_Animal,
	ValueTypeSpec: premadeCodecTypeSpec_string,
    KeyWireType:   thrift.I32,
	ValueWireType: thrift.STRING,
},

    }
    premadeCodecTypeSpec_list_module_Vehicle = &thrift.TypeSpec{
        CodecListSpec: &thrift.CodecListSpec{
    ElementWireType: thrift.STRUCT,
	ElementTypeSpec: premadeCodecTypeSpec_module_Vehicle,
},

    }
    premadeCodecTypeSpec_module_Person = &thrift.TypeSpec{
        CodecStructSpec: &thrift.CodecStructSpec{
    NewFunc: func() thrift.Struct { return NewPerson() },
},

    }
})

// Premade struct specs
var (
    premadeStructSpec_Color *thrift.StructSpec = nil
    premadeStructSpec_Vehicle *thrift.StructSpec = nil
    premadeStructSpec_Person *thrift.StructSpec = nil
)

// Premade struct specs initializer
var premadeStructSpecsInitOnce = sync.OnceFunc(func() {
    premadeStructSpec_Color = &thrift.StructSpec{
    Name:               "Color",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.DOUBLE),
            Name:                 "red",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_double,
            MustBeSetToSerialize: false,
        },        {
            ID:                   2,
            WireType:             thrift.Type(thrift.DOUBLE),
            Name:                 "green",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_double,
            MustBeSetToSerialize: false,
        },        {
            ID:                   3,
            WireType:             thrift.Type(thrift.DOUBLE),
            Name:                 "blue",
            ReflectIndex:         2,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_double,
            MustBeSetToSerialize: false,
        },        {
            ID:                   4,
            WireType:             thrift.Type(thrift.DOUBLE),
            Name:                 "alpha",
            ReflectIndex:         3,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_double,
            MustBeSetToSerialize: false,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
        2: 1,
        3: 2,
        4: 3,
    },
}
    premadeStructSpec_Vehicle = &thrift.StructSpec{
    Name:               "Vehicle",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.STRUCT),
            Name:                 "color",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_Color,
            MustBeSetToSerialize: true,
        },        {
            ID:                   2,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "licensePlate",
            ReflectIndex:         1,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: true,
        },        {
            ID:                   3,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "description",
            ReflectIndex:         2,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: true,
        },        {
            ID:                   4,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "name",
            ReflectIndex:         3,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: true,
        },        {
            ID:                   5,
            WireType:             thrift.Type(thrift.BOOL),
            Name:                 "hasAC",
            ReflectIndex:         4,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_bool,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
    },
}
    premadeStructSpec_Person = &thrift.StructSpec{
    Name:               "Person",
    IsUnion:            false,
    IsException:        false,
    FieldSpecs:         []thrift.FieldSpec{
        {
            ID:                   1,
            WireType:             thrift.Type(thrift.I64),
            Name:                 "id",
            ReflectIndex:         0,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_module_PersonID,
            MustBeSetToSerialize: false,
        },        {
            ID:                   2,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "name",
            ReflectIndex:         1,
            IsOptional:           false,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: false,
        },        {
            ID:                   3,
            WireType:             thrift.Type(thrift.I16),
            Name:                 "age",
            ReflectIndex:         2,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_i16,
            MustBeSetToSerialize: true,
        },        {
            ID:                   4,
            WireType:             thrift.Type(thrift.STRING),
            Name:                 "address",
            ReflectIndex:         3,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_string,
            MustBeSetToSerialize: true,
        },        {
            ID:                   5,
            WireType:             thrift.Type(thrift.STRUCT),
            Name:                 "favoriteColor",
            ReflectIndex:         4,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_module_Color,
            MustBeSetToSerialize: true,
        },        {
            ID:                   6,
            WireType:             thrift.Type(thrift.SET),
            Name:                 "friends",
            ReflectIndex:         5,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_set_module_PersonID,
            MustBeSetToSerialize: true,
        },        {
            ID:                   7,
            WireType:             thrift.Type(thrift.I64),
            Name:                 "bestFriend",
            ReflectIndex:         6,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_module_PersonID,
            MustBeSetToSerialize: true,
        },        {
            ID:                   8,
            WireType:             thrift.Type(thrift.MAP),
            Name:                 "petNames",
            ReflectIndex:         7,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_map_module_Animal_string,
            MustBeSetToSerialize: true,
        },        {
            ID:                   9,
            WireType:             thrift.Type(thrift.I32),
            Name:                 "afraidOfAnimal",
            ReflectIndex:         8,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_module_Animal,
            MustBeSetToSerialize: true,
        },        {
            ID:                   10,
            WireType:             thrift.Type(thrift.LIST),
            Name:                 "vehicles",
            ReflectIndex:         9,
            IsOptional:           true,
            ValueTypeSpec:        premadeCodecTypeSpec_list_module_Vehicle,
            MustBeSetToSerialize: true,
        },    },
    FieldSpecIDToIndex: map[int16]int{
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
    },
}
})

var premadeCodecSpecsMapOnce = sync.OnceValue(
    func() map[string]*thrift.TypeSpec {
        // Relies on premade codec specs initialization
        premadeCodecSpecsInitOnce()
        return map[string]*thrift.TypeSpec{
            "module.Animal": premadeCodecTypeSpec_module_Animal,
            "double": premadeCodecTypeSpec_double,
            "module.Color": premadeCodecTypeSpec_module_Color,
            "string": premadeCodecTypeSpec_string,
            "bool": premadeCodecTypeSpec_bool,
            "module.Vehicle": premadeCodecTypeSpec_module_Vehicle,
            "i64": premadeCodecTypeSpec_i64,
            "module.PersonID": premadeCodecTypeSpec_module_PersonID,
            "i16": premadeCodecTypeSpec_i16,
            "module.Person": premadeCodecTypeSpec_module_Person,
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
