#!/usr/bin/env python3

"""
This module annotates the below function’s parameters
and return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element from the input
    list and its length.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
