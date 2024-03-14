#!/usr/bin/env python3

"""
This module a type-annotated function concat that
takes a string str1 and a string str2 as arguments
and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Returns concatenated string
    Args:
        str1 (str): first string to be concatenated
        str2 (str): second string to be concatenated
    Return:
        concatenation of str1 and str2
    """
    return str1 + str2
