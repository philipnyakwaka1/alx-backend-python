#!/usr/bin/env python3

"""
This module defines a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats and returns
their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Finds the average sum of elements of a mixed list of ints and floats
    Args:
    mxd_list (list): List whose sum is to be founds
    Return:
        Sum of elements of input_list
    """
    return sum(mxd_list)
