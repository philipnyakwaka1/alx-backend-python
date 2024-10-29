#!/usr/bin/env python3

"""
This module defines a type-annotated function to_kv that takes
a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k. The second element
is the square of the int/float v and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string and float or int as argument and returns a tup
    Args:
        k (str): input string
        v (Union[int, float]): input int or float
    Return:
        (str, v ** 2)
    """
    return (k, float(v ** 2))
