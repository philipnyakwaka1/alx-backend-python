#!/usr/bin/env python3

"""
This module contains a type-annotated function
floor which takes a float n as argument and
returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    Floors a number
    Args:
        n (float): number to be floored
    Return:
        floor of n
    """
    return math.floor(n)
