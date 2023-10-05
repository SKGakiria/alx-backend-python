#!/usr/bin/env python3
"""Module containing function with the correct duck-typed annotations"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function returns the annotated results"""
    if lst:
        return lst[0]
    else:
        return None
