#!/usr/bin/env python3
"""This modules annotates a function"""
from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuple containg each iterable element and its length
    Args:
        lst (iterable): Iterable
    Returns:
        list: List of tuple containg each iterable element and its length
    """

    return [(i, len(i)) for i in lst]
