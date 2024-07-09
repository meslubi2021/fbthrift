#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/constants/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import thrift.py3.types
import importlib
from collections.abc import Sequence

"""
    This is a helper module to define py3 container types.
    All types defined here are re-exported in the parent `.types` module.
    Only `import` types defined here via the parent `.types` module.
    If you `import` them directly from here, you will get nasty import errors.
"""

import module.types as _module_types

def get_types_reflection():
    return importlib.import_module(
        "module.types_reflection"
    )

__all__ = []

class List__i32(thrift.py3.types.List):
    __slots__ = []

    def __init__(self, items=None, private_ctor_token=None) -> None:
        if private_ctor_token is thrift.py3.types._fbthrift_list_private_ctor:
            _py_obj = items
        elif isinstance(items, List__i32):
            _py_obj = list(items)
        elif items is None:
            _py_obj = []
        else:
            check_method = List__i32._check_item_type_or_raise
            _py_obj = [check_method(item) for item in items]

        super().__init__(_py_obj, List__i32)

    @staticmethod
    def _check_item_type_or_raise(item):
        if not (
            isinstance(item, int)
        ):
            raise TypeError(f"{item!r} is not of type int")
        return item

    @staticmethod
    def _check_item_type_or_none(item):
        if item is None:
            return None
        if isinstance(item, int):
            return item

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__List__i32()


Sequence.register(List__i32)
__all__.append('List__i32')

class List__Map__string_i32(thrift.py3.types.List):
    __slots__ = []

    def __init__(self, items=None, private_ctor_token=None) -> None:
        if private_ctor_token is thrift.py3.types._fbthrift_list_private_ctor:
            _py_obj = items
        elif isinstance(items, List__Map__string_i32):
            _py_obj = list(items)
        elif items is None:
            _py_obj = []
        else:
            check_method = List__Map__string_i32._check_item_type_or_raise
            _py_obj = [check_method(item) for item in items]

        super().__init__(_py_obj, List__Map__string_i32)

    @staticmethod
    def _check_item_type_or_raise(item):
        if item is None:
            raise TypeError("None is not of the type _typing.Mapping[str, int]")
        if not isinstance(item, _module_types.Map__string_i32):
            item = _module_types.Map__string_i32(item)
        return item

    @staticmethod
    def _check_item_type_or_none(item):
        if item is None:
            return None
        if isinstance(item, _module_types.Map__string_i32):
            return item
        try:
            return _module_types.Map__string_i32(item)
        except:
            pass

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__List__Map__string_i32()


Sequence.register(List__Map__string_i32)
__all__.append('List__Map__string_i32')

class List__Range(thrift.py3.types.List):
    __slots__ = []

    def __init__(self, items=None, private_ctor_token=None) -> None:
        if private_ctor_token is thrift.py3.types._fbthrift_list_private_ctor:
            _py_obj = items
        elif isinstance(items, List__Range):
            _py_obj = list(items)
        elif items is None:
            _py_obj = []
        else:
            check_method = List__Range._check_item_type_or_raise
            _py_obj = [check_method(item) for item in items]

        super().__init__(_py_obj, List__Range)

    @staticmethod
    def _check_item_type_or_raise(item):
        if not (
            isinstance(item, _module_types.Range)
        ):
            raise TypeError(f"{item!r} is not of type _module_types.Range")
        return item

    @staticmethod
    def _check_item_type_or_none(item):
        if item is None:
            return None
        if isinstance(item, _module_types.Range):
            return item

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__List__Range()


Sequence.register(List__Range)
__all__.append('List__Range')

class List__Internship(thrift.py3.types.List):
    __slots__ = []

    def __init__(self, items=None, private_ctor_token=None) -> None:
        if private_ctor_token is thrift.py3.types._fbthrift_list_private_ctor:
            _py_obj = items
        elif isinstance(items, List__Internship):
            _py_obj = list(items)
        elif items is None:
            _py_obj = []
        else:
            check_method = List__Internship._check_item_type_or_raise
            _py_obj = [check_method(item) for item in items]

        super().__init__(_py_obj, List__Internship)

    @staticmethod
    def _check_item_type_or_raise(item):
        if not (
            isinstance(item, _module_types.Internship)
        ):
            raise TypeError(f"{item!r} is not of type _module_types.Internship")
        return item

    @staticmethod
    def _check_item_type_or_none(item):
        if item is None:
            return None
        if isinstance(item, _module_types.Internship):
            return item

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__List__Internship()


Sequence.register(List__Internship)
__all__.append('List__Internship')

class List__string(thrift.py3.types.List):
    __slots__ = []

    def __init__(self, items=None, private_ctor_token=None) -> None:
        if private_ctor_token is thrift.py3.types._fbthrift_list_private_ctor:
            _py_obj = items
        elif isinstance(items, List__string):
            _py_obj = list(items)
        elif items is None:
            _py_obj = []
        else:
            if isinstance(items, str):
                raise TypeError("If you really want to pass a string into a _typing.Sequence[str] field, explicitly convert it first.")
            check_method = List__string._check_item_type_or_raise
            _py_obj = [check_method(item) for item in items]

        super().__init__(_py_obj, List__string)

    @staticmethod
    def _check_item_type_or_raise(item):
        if not (
            isinstance(item, str)
        ):
            raise TypeError(f"{item!r} is not of type str")
        return item

    @staticmethod
    def _check_item_type_or_none(item):
        if item is None:
            return None
        if isinstance(item, str):
            return item

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__List__string()


Sequence.register(List__string)
__all__.append('List__string')

