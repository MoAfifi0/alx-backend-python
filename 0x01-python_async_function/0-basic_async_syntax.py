#!/usr/bin/env python3
"""
    wait_random is a function that wait for a random delay between
    0 and max_delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay
      (included and float value)
    seconds and eventually returns it.

    Args:
    max_delay: the maximum of the random delay

    Returns:
    the new delay in seconde
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
