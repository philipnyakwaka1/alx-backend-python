#!/usr/bin/env python3
"""
Module containing a type-annotated function that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a given multiplier
    Args:
        multiplier (float): The multiplier to be used
    Returns:
        Callable[[float], float]: A function that takes a float as argument and
        returns the product of the float by
    """
    def multiplier_function(n: float) -> float:
        """
        Return the product of input float and the multiplier
        Args:
            n (float): Float to be multiplied by the multiplier
        Returns:
            float: product of input float and the multipier
        """

        return multiplier * n

    return multiplier_function
