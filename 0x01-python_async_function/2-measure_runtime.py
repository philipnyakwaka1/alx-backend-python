#!/usr/bin/env python3

"""
This module defines a measure_time function with integers n
and max_delay as arguments that measures the total execution
time for wait_n(n, max_delay), and returns total_time / n
"""

import asyncio
import time
wait_random = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function has integers n and max_delay as arguments that measures
    the total execution time for wait_n(n, max_delay), and returns
    total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_random(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
