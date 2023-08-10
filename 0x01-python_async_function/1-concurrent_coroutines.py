#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times.

    Args:
    n: the number of times wait_random should be execute
    max_delay: the delay in seconde

    Returns:
    a list of all the delay during the runtime
    """

    background_task = []

    for i in range(n):
        random_delay = asyncio.create_task(wait_random(max_delay))
        background_task.append(random_delay)

    return [await task for task in asyncio.as_completed(background_task)]
