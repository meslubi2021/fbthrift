#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import apache.thrift.metadata.thrift_types as _fbthrift_metadata


# TODO (ffrancet): This general pattern can be optimized by using tuples and dicts
# instead of re-generating thrift structs
def _fbthrift_gen_metadata_struct_TemplateLists(metadata_struct: _fbthrift_metadata.ThriftMetadata) -> _fbthrift_metadata.ThriftMetadata:
    qualified_name = "containers.TemplateLists"

    if qualified_name in metadata_struct.structs:
        return metadata_struct
    fields = [
        _fbthrift_metadata.ThriftField(id=1, type=_fbthrift_metadata.ThriftType(t_list=_fbthrift_metadata.ThriftListType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="std_string", is_optional=True, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="std::vector"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=2, type=_fbthrift_metadata.ThriftType(t_list=_fbthrift_metadata.ThriftListType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_BINARY_TYPE))), name="deque_string", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="std::deque"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=3, type=_fbthrift_metadata.ThriftType(t_list=_fbthrift_metadata.ThriftListType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_BINARY_TYPE))), name="small_vector_iobuf", is_optional=False, structured_annotations=[
        ]),
        _fbthrift_metadata.ThriftField(id=4, type=_fbthrift_metadata.ThriftType(t_list=_fbthrift_metadata.ThriftListType(valueType=_fbthrift_metadata.ThriftType(t_list=_fbthrift_metadata.ThriftListType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))))), name="nested_small_vector", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::small_vector"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=5, type=_fbthrift_metadata.ThriftType(t_list=_fbthrift_metadata.ThriftListType(valueType=_fbthrift_metadata.ThriftType(t_list=_fbthrift_metadata.ThriftListType(valueType=_fbthrift_metadata.ThriftType(t_list=_fbthrift_metadata.ThriftListType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))))))), name="small_vector_tensor", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::fbvector"),  }),
        ]),
    ]
    struct_dict = dict(metadata_struct.structs)
    struct_dict[qualified_name] = _fbthrift_metadata.ThriftStruct(name=qualified_name, fields=fields,
        is_union=False,
        structured_annotations=[
        ])
    new_struct = metadata_struct(structs=struct_dict)

     # std_string
     # deque_string
     # small_vector_iobuf
     # nested_small_vector
     # small_vector_tensor

    return new_struct
def gen_metadata_struct_TemplateLists() -> _fbthrift_metadata.ThriftMetadata:
    return _fbthrift_gen_metadata_struct_TemplateLists(_fbthrift_metadata.ThriftMetadata(structs={}, enums={}, exceptions={}, services={}))

# TODO (ffrancet): This general pattern can be optimized by using tuples and dicts
# instead of re-generating thrift structs
def _fbthrift_gen_metadata_struct_TemplateSets(metadata_struct: _fbthrift_metadata.ThriftMetadata) -> _fbthrift_metadata.ThriftMetadata:
    qualified_name = "containers.TemplateSets"

    if qualified_name in metadata_struct.structs:
        return metadata_struct
    fields = [
        _fbthrift_metadata.ThriftField(id=1, type=_fbthrift_metadata.ThriftType(t_set=_fbthrift_metadata.ThriftSetType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="std_set", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="std::set"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=2, type=_fbthrift_metadata.ThriftType(t_set=_fbthrift_metadata.ThriftSetType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="std_unordered", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="std::unordered_set"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=3, type=_fbthrift_metadata.ThriftType(t_set=_fbthrift_metadata.ThriftSetType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_fast", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::F14FastSet"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=4, type=_fbthrift_metadata.ThriftType(t_set=_fbthrift_metadata.ThriftSetType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_node", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::F14NodeSet"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=5, type=_fbthrift_metadata.ThriftType(t_set=_fbthrift_metadata.ThriftSetType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_value", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::F14ValueSet"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=6, type=_fbthrift_metadata.ThriftType(t_set=_fbthrift_metadata.ThriftSetType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_vector", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::F14VectorSet"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=7, type=_fbthrift_metadata.ThriftType(t_set=_fbthrift_metadata.ThriftSetType(valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_sorted_vector", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::sorted_vector_set"),  }),
        ]),
    ]
    struct_dict = dict(metadata_struct.structs)
    struct_dict[qualified_name] = _fbthrift_metadata.ThriftStruct(name=qualified_name, fields=fields,
        is_union=False,
        structured_annotations=[
        ])
    new_struct = metadata_struct(structs=struct_dict)

     # std_set
     # std_unordered
     # folly_fast
     # folly_node
     # folly_value
     # folly_vector
     # folly_sorted_vector

    return new_struct
def gen_metadata_struct_TemplateSets() -> _fbthrift_metadata.ThriftMetadata:
    return _fbthrift_gen_metadata_struct_TemplateSets(_fbthrift_metadata.ThriftMetadata(structs={}, enums={}, exceptions={}, services={}))

# TODO (ffrancet): This general pattern can be optimized by using tuples and dicts
# instead of re-generating thrift structs
def _fbthrift_gen_metadata_struct_TemplateMaps(metadata_struct: _fbthrift_metadata.ThriftMetadata) -> _fbthrift_metadata.ThriftMetadata:
    qualified_name = "containers.TemplateMaps"

    if qualified_name in metadata_struct.structs:
        return metadata_struct
    fields = [
        _fbthrift_metadata.ThriftField(id=1, type=_fbthrift_metadata.ThriftType(t_map=_fbthrift_metadata.ThriftMapType(keyType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE),valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="std_map", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="std::map"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=2, type=_fbthrift_metadata.ThriftType(t_map=_fbthrift_metadata.ThriftMapType(keyType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE),valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="std_unordered", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="std::unordered_map"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=3, type=_fbthrift_metadata.ThriftType(t_map=_fbthrift_metadata.ThriftMapType(keyType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE),valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_fast", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::F14FastMap"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=4, type=_fbthrift_metadata.ThriftType(t_map=_fbthrift_metadata.ThriftMapType(keyType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE),valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_node", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::F14NodeMap"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=5, type=_fbthrift_metadata.ThriftType(t_map=_fbthrift_metadata.ThriftMapType(keyType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE),valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_value", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::F14ValueMap"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=6, type=_fbthrift_metadata.ThriftType(t_map=_fbthrift_metadata.ThriftMapType(keyType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE),valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_vector", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::F14VectorMap"),  }),
        ]),
        _fbthrift_metadata.ThriftField(id=7, type=_fbthrift_metadata.ThriftType(t_map=_fbthrift_metadata.ThriftMapType(keyType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE),valueType=_fbthrift_metadata.ThriftType(t_primitive=_fbthrift_metadata.ThriftPrimitiveType.THRIFT_STRING_TYPE))), name="folly_sorted_vector", is_optional=False, structured_annotations=[
            _fbthrift_metadata.ThriftConstStruct(type=_fbthrift_metadata.ThriftStructType(name="cpp.Type"), fields= { "template": _fbthrift_metadata.ThriftConstValue(cv_string="folly::sorted_vector_map"),  }),
        ]),
    ]
    struct_dict = dict(metadata_struct.structs)
    struct_dict[qualified_name] = _fbthrift_metadata.ThriftStruct(name=qualified_name, fields=fields,
        is_union=False,
        structured_annotations=[
        ])
    new_struct = metadata_struct(structs=struct_dict)

     # key
     # val  # std_map
     # key
     # val  # std_unordered
     # key
     # val  # folly_fast
     # key
     # val  # folly_node
     # key
     # val  # folly_value
     # key
     # val  # folly_vector
     # key
     # val  # folly_sorted_vector

    return new_struct
def gen_metadata_struct_TemplateMaps() -> _fbthrift_metadata.ThriftMetadata:
    return _fbthrift_gen_metadata_struct_TemplateMaps(_fbthrift_metadata.ThriftMetadata(structs={}, enums={}, exceptions={}, services={}))




def getThriftModuleMetadata() -> _fbthrift_metadata.ThriftMetadata:
    meta = _fbthrift_metadata.ThriftMetadata(structs={}, enums={}, exceptions={}, services={})
    meta = _fbthrift_gen_metadata_struct_TemplateLists(meta)
    meta = _fbthrift_gen_metadata_struct_TemplateSets(meta)
    meta = _fbthrift_gen_metadata_struct_TemplateMaps(meta)
    return meta
