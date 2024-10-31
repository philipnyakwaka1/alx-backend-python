#!/usr/bin/env python3
"""
This module contains a type-annotated function to return the floor of a float
"""
import math


def floor(n: float) -> int:
    """
    Return the floor of a float
    Args:
        n (float): number whose floor is to be returned
    Return:
        int: floor of the argument
    """

    return math.floor(n)
