#!/usr/bin/env python3

"""
This module defines a type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Finds the average sum of elements of a list of floats
    Args:
        input_list (list): List whose sum is to be founds
    Return:
        Sum of elements of input_list
    """
    return sum(input_list)
