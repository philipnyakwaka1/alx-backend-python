#!/usr/bin/env python3

"""
This module augments the following code with the
correct duck-typed annotations
"""
from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence safely or None if
    the sequence is empty.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
