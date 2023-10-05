#!/usr/bin/env python3
"""Module containing function that multiplies a float by a multipier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function returns a function that multiplies a float by multiplier"""
    def multiplier_func(num: float) -> float:
        """Function multiplies a float by multiplier"""
        return num * multiplier

    return multiplier_func
