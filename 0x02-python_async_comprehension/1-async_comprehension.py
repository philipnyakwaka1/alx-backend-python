#!/usr/bin/env python3
"""
This module imports async_generator from the previous task and
then writes a coroutine called async_comprehension that takes no arguments.
"""
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    return [i async for i in async_generator()]
