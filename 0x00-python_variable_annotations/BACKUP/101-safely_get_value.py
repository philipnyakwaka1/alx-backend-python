#!/usr/bin/env python3

"""
This module augments the following code with the
correct duck-typed annotations
"""
from typing import Mapping, Any, Union, TypeVar, Optional


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely gets the value from a dictionary for a given key.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to search for in the dictionary.
        default (Optional): The default value to return if the key is not found (default is None).

    Returns:
        Union[Any, T]: The value corresponding to the key in the dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
