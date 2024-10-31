#!/usr/bin/env python3
"""
Module containing function to sum all elements of a list
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Return sum of elements in a list of floats
    Args:
        my_list (list): List of floats whose elements are to be summed
    Returns:
        float: sum of all elements in the argument list
    """

    return sum(mxd_list)
