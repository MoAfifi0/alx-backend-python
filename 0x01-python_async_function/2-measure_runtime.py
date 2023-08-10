#!/usr/bin/env python3
"""Measure the runtime
"""
from asyncio import run
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return the average runtime of wait_n.

    Args:
    n: the number of times the wait-random should be execute
    max_delay: the delay in seconde

    Return:
    return the runtime

    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    return (end_time - start_time) / n
