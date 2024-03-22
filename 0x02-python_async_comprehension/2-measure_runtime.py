#!/usr/bin/env Python3
"""
This module import async_comprehension from the previous file
and writes a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""

from typing import Callable, Awaitable, List
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """This function measures the total runtime and return it"""
    start = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    stop = time.time()
    return stop - start
