#!/usr/bin/env python3

"""
This module defines type-annotated function make_multiplier
that takes a float multiplier as argument and returns a function
that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that takes a float as input
        and returns the result of multiplying it by the given multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the given multiplier.

        Args:
            x (float): The float to be multiplied.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function
