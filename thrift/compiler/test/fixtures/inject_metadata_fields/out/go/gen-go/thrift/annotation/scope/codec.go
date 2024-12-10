// Autogenerated by Thrift for thrift/annotation/scope.thrift
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//  @generated

package scope


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
    premadeCodecTypeSpec_scope_Transitive *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Program *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Struct *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Union *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Exception *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Field *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Typedef *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Service *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Interaction *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Function *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_EnumValue *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Const *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Enum *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Structured *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Interface *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_RootDefinition *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_Definition *thrift.TypeSpec = nil
    premadeCodecTypeSpec_scope_DisableSchemaConst *thrift.TypeSpec = nil
)

// Premade codec specs initializer
var premadeCodecSpecsInitOnce = sync.OnceFunc(func() {
    premadeCodecTypeSpec_scope_Transitive = &thrift.TypeSpec{
        FullName: "scope.Transitive",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Transitive",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewTransitive() },
},

    }
    premadeCodecTypeSpec_scope_Program = &thrift.TypeSpec{
        FullName: "scope.Program",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Program",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewProgram() },
},

    }
    premadeCodecTypeSpec_scope_Struct = &thrift.TypeSpec{
        FullName: "scope.Struct",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Struct",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewStruct() },
},

    }
    premadeCodecTypeSpec_scope_Union = &thrift.TypeSpec{
        FullName: "scope.Union",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Union",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewUnion() },
},

    }
    premadeCodecTypeSpec_scope_Exception = &thrift.TypeSpec{
        FullName: "scope.Exception",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Exception",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewException() },
},

    }
    premadeCodecTypeSpec_scope_Field = &thrift.TypeSpec{
        FullName: "scope.Field",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Field",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewField() },
},

    }
    premadeCodecTypeSpec_scope_Typedef = &thrift.TypeSpec{
        FullName: "scope.Typedef",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Typedef",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewTypedef() },
},

    }
    premadeCodecTypeSpec_scope_Service = &thrift.TypeSpec{
        FullName: "scope.Service",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Service",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewService() },
},

    }
    premadeCodecTypeSpec_scope_Interaction = &thrift.TypeSpec{
        FullName: "scope.Interaction",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Interaction",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewInteraction() },
},

    }
    premadeCodecTypeSpec_scope_Function = &thrift.TypeSpec{
        FullName: "scope.Function",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Function",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewFunction() },
},

    }
    premadeCodecTypeSpec_scope_EnumValue = &thrift.TypeSpec{
        FullName: "scope.EnumValue",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.EnumValue",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewEnumValue() },
},

    }
    premadeCodecTypeSpec_scope_Const = &thrift.TypeSpec{
        FullName: "scope.Const",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Const",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewConst() },
},

    }
    premadeCodecTypeSpec_scope_Enum = &thrift.TypeSpec{
        FullName: "scope.Enum",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Enum",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewEnum() },
},

    }
    premadeCodecTypeSpec_scope_Structured = &thrift.TypeSpec{
        FullName: "scope.Structured",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Structured",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewStructured() },
},

    }
    premadeCodecTypeSpec_scope_Interface = &thrift.TypeSpec{
        FullName: "scope.Interface",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Interface",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewInterface() },
},

    }
    premadeCodecTypeSpec_scope_RootDefinition = &thrift.TypeSpec{
        FullName: "scope.RootDefinition",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.RootDefinition",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewRootDefinition() },
},

    }
    premadeCodecTypeSpec_scope_Definition = &thrift.TypeSpec{
        FullName: "scope.Definition",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.Definition",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewDefinition() },
},

    }
    premadeCodecTypeSpec_scope_DisableSchemaConst = &thrift.TypeSpec{
        FullName: "scope.DisableSchemaConst",
        CodecStructSpec: &thrift.CodecStructSpec{
    ScopedName: "scope.DisableSchemaConst",
    IsUnion:    false,
    NewFunc:    func() thrift.Struct { return NewDisableSchemaConst() },
},

    }
})

// Premade struct specs
var (
    premadeStructSpec_Transitive *thrift.StructSpec = nil
    premadeStructSpec_Program *thrift.StructSpec = nil
    premadeStructSpec_Struct *thrift.StructSpec = nil
    premadeStructSpec_Union *thrift.StructSpec = nil
    premadeStructSpec_Exception *thrift.StructSpec = nil
    premadeStructSpec_Field *thrift.StructSpec = nil
    premadeStructSpec_Typedef *thrift.StructSpec = nil
    premadeStructSpec_Service *thrift.StructSpec = nil
    premadeStructSpec_Interaction *thrift.StructSpec = nil
    premadeStructSpec_Function *thrift.StructSpec = nil
    premadeStructSpec_EnumValue *thrift.StructSpec = nil
    premadeStructSpec_Const *thrift.StructSpec = nil
    premadeStructSpec_Enum *thrift.StructSpec = nil
    premadeStructSpec_Structured *thrift.StructSpec = nil
    premadeStructSpec_Interface *thrift.StructSpec = nil
    premadeStructSpec_RootDefinition *thrift.StructSpec = nil
    premadeStructSpec_Definition *thrift.StructSpec = nil
    premadeStructSpec_DisableSchemaConst *thrift.StructSpec = nil
)

// Premade struct specs initializer
var premadeStructSpecsInitOnce = sync.OnceFunc(func() {
    premadeStructSpec_Transitive = &thrift.StructSpec{
    Name:                 "Transitive",
    ScopedName:           "scope.Transitive",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Program = &thrift.StructSpec{
    Name:                 "Program",
    ScopedName:           "scope.Program",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Struct = &thrift.StructSpec{
    Name:                 "Struct",
    ScopedName:           "scope.Struct",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Union = &thrift.StructSpec{
    Name:                 "Union",
    ScopedName:           "scope.Union",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Exception = &thrift.StructSpec{
    Name:                 "Exception",
    ScopedName:           "scope.Exception",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Field = &thrift.StructSpec{
    Name:                 "Field",
    ScopedName:           "scope.Field",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Typedef = &thrift.StructSpec{
    Name:                 "Typedef",
    ScopedName:           "scope.Typedef",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Service = &thrift.StructSpec{
    Name:                 "Service",
    ScopedName:           "scope.Service",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Interaction = &thrift.StructSpec{
    Name:                 "Interaction",
    ScopedName:           "scope.Interaction",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Function = &thrift.StructSpec{
    Name:                 "Function",
    ScopedName:           "scope.Function",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_EnumValue = &thrift.StructSpec{
    Name:                 "EnumValue",
    ScopedName:           "scope.EnumValue",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Const = &thrift.StructSpec{
    Name:                 "Const",
    ScopedName:           "scope.Const",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Enum = &thrift.StructSpec{
    Name:                 "Enum",
    ScopedName:           "scope.Enum",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Structured = &thrift.StructSpec{
    Name:                 "Structured",
    ScopedName:           "scope.Structured",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Interface = &thrift.StructSpec{
    Name:                 "Interface",
    ScopedName:           "scope.Interface",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_RootDefinition = &thrift.StructSpec{
    Name:                 "RootDefinition",
    ScopedName:           "scope.RootDefinition",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_Definition = &thrift.StructSpec{
    Name:                 "Definition",
    ScopedName:           "scope.Definition",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
    premadeStructSpec_DisableSchemaConst = &thrift.StructSpec{
    Name:                 "DisableSchemaConst",
    ScopedName:           "scope.DisableSchemaConst",
    IsUnion:              false,
    IsException:          false,
    FieldSpecs:           []thrift.FieldSpec{
    },
    FieldSpecIDToIndex:   map[int16]int{
    },
    FieldSpecNameToIndex: map[string]int{
    },
}
})

// Premade slice of all struct specs
var premadeStructSpecsOnce = sync.OnceValue(
    func() []*thrift.StructSpec {
        // Relies on premade struct specs
        premadeStructSpecsInitOnce()

        fbthriftResults := make([]*thrift.StructSpec, 0)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Transitive)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Program)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Struct)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Union)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Exception)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Field)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Typedef)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Service)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Interaction)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Function)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_EnumValue)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Const)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Enum)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Structured)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Interface)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_RootDefinition)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_Definition)
        fbthriftResults = append(fbthriftResults, premadeStructSpec_DisableSchemaConst)
        return fbthriftResults
    },
)

var premadeCodecSpecsMapOnce = sync.OnceValue(
    func() map[string]*thrift.TypeSpec {
        // Relies on premade codec specs initialization
        premadeCodecSpecsInitOnce()

        fbthriftTypeSpecsMap := make(map[string]*thrift.TypeSpec)
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Transitive.FullName] = premadeCodecTypeSpec_scope_Transitive
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Program.FullName] = premadeCodecTypeSpec_scope_Program
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Struct.FullName] = premadeCodecTypeSpec_scope_Struct
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Union.FullName] = premadeCodecTypeSpec_scope_Union
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Exception.FullName] = premadeCodecTypeSpec_scope_Exception
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Field.FullName] = premadeCodecTypeSpec_scope_Field
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Typedef.FullName] = premadeCodecTypeSpec_scope_Typedef
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Service.FullName] = premadeCodecTypeSpec_scope_Service
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Interaction.FullName] = premadeCodecTypeSpec_scope_Interaction
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Function.FullName] = premadeCodecTypeSpec_scope_Function
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_EnumValue.FullName] = premadeCodecTypeSpec_scope_EnumValue
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Const.FullName] = premadeCodecTypeSpec_scope_Const
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Enum.FullName] = premadeCodecTypeSpec_scope_Enum
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Structured.FullName] = premadeCodecTypeSpec_scope_Structured
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Interface.FullName] = premadeCodecTypeSpec_scope_Interface
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_RootDefinition.FullName] = premadeCodecTypeSpec_scope_RootDefinition
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_Definition.FullName] = premadeCodecTypeSpec_scope_Definition
        fbthriftTypeSpecsMap[premadeCodecTypeSpec_scope_DisableSchemaConst.FullName] = premadeCodecTypeSpec_scope_DisableSchemaConst
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
