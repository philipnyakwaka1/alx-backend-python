#!/usr/bin/env Python3
"""
This module import async_comprehension from the previous file
and writes a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""

from typing import Awaitable, List
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function measures the total runtime and return it"""
    start: float = time.time()
    t: List[Awaitable[List[float]]] = [async_comprehension() for i in range(4)]
    await asyncio.gather(*t)
    stop = time.time()
    return stop - start
