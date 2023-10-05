#!/usr/bin/env python3
"""Module containing function that sums the list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function returns the sum of a list of floats"""
    if input_list is None:
        return 0
    else:
        return sum(input_list)
