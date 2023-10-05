#!/usr/bin/env python3
"""Module containing function that creates a tuple from
a string and an int/float"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function returns a tuple"""
    return k, v ** 2
