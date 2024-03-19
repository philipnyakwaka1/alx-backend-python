#!/usr/bin/env python3

"""
This module takes the code from wait_n and alters it into
a new function task_wait_n. The code is nearly identical to wait_n
except task_wait_random is being called.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This functions takes the code from wait_n and alters it
    into a new function task_wait_n. The code is nearly identical to wait_n
    except task_wait_random is being called.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*tasks)
    return sorted(result)
