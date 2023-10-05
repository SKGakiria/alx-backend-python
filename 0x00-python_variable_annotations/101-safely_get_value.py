#!/usr/bin/env python3
"""Module containing function with the correct type annotation"""
from typing import Any, Mapping, TypeVar, Union, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Function returns a value from a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
