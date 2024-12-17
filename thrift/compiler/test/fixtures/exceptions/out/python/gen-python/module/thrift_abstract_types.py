

#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import abc as _abc
import typing as _typing

_fbthrift_property = property


import folly.iobuf as _fbthrift_iobuf
import thrift.python.abstract_types as _fbthrift_python_abstract_types

class Fiery(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def message(self) -> str: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Fiery": ...  # type: ignore
    def _to_python(self) -> "module.thrift_types.Fiery": ...  # type: ignore
    def _to_py3(self) -> "module.types.Fiery": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Fiery": ...  # type: ignore
_fbthrift_Fiery = Fiery
class Serious(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def not_sonnet(self) -> _typing.Optional[str]: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Serious": ...  # type: ignore
    def _to_python(self) -> "module.thrift_types.Serious": ...  # type: ignore
    def _to_py3(self) -> "module.types.Serious": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Serious": ...  # type: ignore
_fbthrift_Serious = Serious
class ComplexFieldNames(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def error_message(self) -> str: ...
    @_fbthrift_property
    def internal_error_message(self) -> str: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.ComplexFieldNames": ...  # type: ignore
    def _to_python(self) -> "module.thrift_types.ComplexFieldNames": ...  # type: ignore
    def _to_py3(self) -> "module.types.ComplexFieldNames": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ComplexFieldNames": ...  # type: ignore
_fbthrift_ComplexFieldNames = ComplexFieldNames
class CustomFieldNames(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def error_message(self) -> str: ...
    @_fbthrift_property
    def internal_error_message(self) -> str: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.CustomFieldNames": ...  # type: ignore
    def _to_python(self) -> "module.thrift_types.CustomFieldNames": ...  # type: ignore
    def _to_py3(self) -> "module.types.CustomFieldNames": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.CustomFieldNames": ...  # type: ignore
_fbthrift_CustomFieldNames = CustomFieldNames
class ExceptionWithPrimitiveField(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def message(self) -> str: ...
    @_fbthrift_property
    def error_code(self) -> int: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.ExceptionWithPrimitiveField": ...  # type: ignore
    def _to_python(self) -> "module.thrift_types.ExceptionWithPrimitiveField": ...  # type: ignore
    def _to_py3(self) -> "module.types.ExceptionWithPrimitiveField": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ExceptionWithPrimitiveField": ...  # type: ignore
_fbthrift_ExceptionWithPrimitiveField = ExceptionWithPrimitiveField
class ExceptionWithStructuredAnnotation(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def message_field(self) -> str: ...
    @_fbthrift_property
    def error_code(self) -> int: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.ExceptionWithStructuredAnnotation": ...  # type: ignore
    def _to_python(self) -> "module.thrift_types.ExceptionWithStructuredAnnotation": ...  # type: ignore
    def _to_py3(self) -> "module.types.ExceptionWithStructuredAnnotation": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ExceptionWithStructuredAnnotation": ...  # type: ignore
_fbthrift_ExceptionWithStructuredAnnotation = ExceptionWithStructuredAnnotation
class Banal(_fbthrift_python_abstract_types.AbstractGeneratedError):
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Banal": ...  # type: ignore
    def _to_python(self) -> "module.thrift_types.Banal": ...  # type: ignore
    def _to_py3(self) -> "module.types.Banal": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Banal": ...  # type: ignore
_fbthrift_Banal = Banal
