#!/usr/bin/env python3
"""Module containing function with annotated parameters"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Function returns values with the appropriate types"""
    return [(i, len(i)) for i in lst]
