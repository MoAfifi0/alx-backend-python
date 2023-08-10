#!/usr/bin/env python3
"""task_wait_n
    a function that takes an integer max_delay and returns a asyncio.Task
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times

    Args:
    n: the number of times the wait_random should be executed
    max_delay: the delay in seconde.

    Returns:
    A sorted List of asynchronous task
    """
    delay_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delay_times)
