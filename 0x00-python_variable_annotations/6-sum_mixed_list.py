#!/usr/bin/env python3
"""Module containing function that sums the list of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function returns the sum as a float"""
    return sum(mxd_lst)
