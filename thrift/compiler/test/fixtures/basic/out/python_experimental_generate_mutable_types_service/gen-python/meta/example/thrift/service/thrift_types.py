#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import folly.iobuf as _fbthrift_iobuf
import thrift.python.types as _fbthrift_python_types
import thrift.python.exceptions as _fbthrift_python_exceptions



class EchoRequest(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "text",  # name
            "text",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "service.EchoRequest"

    @staticmethod
    def __get_thrift_uri__():
        return None

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_EchoRequest()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("meta.example.thrift.service.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.EchoRequest, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("meta.example.thrift.service.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.EchoRequest, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("service.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.EchoRequest, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("service.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.EchoRequest, self)


class EchoResponse(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "text",  # name
            "text",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "service.EchoResponse"

    @staticmethod
    def __get_thrift_uri__():
        return None

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_EchoResponse()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("meta.example.thrift.service.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.EchoResponse, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("meta.example.thrift.service.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.EchoResponse, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("service.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.EchoResponse, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("service.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.EchoResponse, self)


class WhisperException(metaclass=_fbthrift_python_exceptions.GeneratedErrorMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "message",  # name
            "message",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "service.WhisperException"

    @staticmethod
    def __get_thrift_uri__():
        return None

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__exception_WhisperException()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("meta.example.thrift.service.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.WhisperException, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("meta.example.thrift.service.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.WhisperException, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("service.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.WhisperException, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("service.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.WhisperException, self)

# This unfortunately has to be down here to prevent circular imports
import meta.example.thrift.service.thrift_metadata


_fbthrift_all_enums = [
]

def _fbthrift_metadata__struct_EchoRequest():
    return meta.example.thrift.service.thrift_metadata.gen_metadata_struct_EchoRequest()


def _fbthrift_metadata__struct_EchoResponse():
    return meta.example.thrift.service.thrift_metadata.gen_metadata_struct_EchoResponse()


def _fbthrift_metadata__exception_WhisperException():
    return meta.example.thrift.service.thrift_metadata.gen_metadata_exception_WhisperException()


_fbthrift_all_structs = [
    EchoRequest,
    EchoResponse,
    WhisperException,
]
_fbthrift_python_types.fill_specs(*_fbthrift_all_structs)



class _fbthrift_EchoService_echo_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "request",  # name
            "request",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(EchoRequest),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_EchoService_echo_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            0,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "success",  # name
            "success", # name
            lambda: _fbthrift_python_types.StructTypeInfo(EchoResponse),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
        ),
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "ex",  # name
            "ex",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(WhisperException),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
    )



_fbthrift_python_types.fill_specs(
    _fbthrift_EchoService_echo_args,
    _fbthrift_EchoService_echo_result,
)
