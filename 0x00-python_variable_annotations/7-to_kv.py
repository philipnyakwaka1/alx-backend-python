#!/usr/bin/env python3
"""
Module defining a function hat takes a string k and an
int OR float v as arguments and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of str and float
    Args:
        k: string argument to returned as the tuple's first index
        v: string or float argument to be squared are returned as tuple's
        second index
    Returns:
        tuple: input string as first index and the square of the
        second argument as float
    """

    return (k, float(v**2))
