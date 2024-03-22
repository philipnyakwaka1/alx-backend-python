#!/usr/bin/env python3
"""
This module imports async_generator from the previous task and
then writes a coroutine called async_comprehension that takes no arguments.
"""
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    This coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    return [i async for i in async_generator()]
