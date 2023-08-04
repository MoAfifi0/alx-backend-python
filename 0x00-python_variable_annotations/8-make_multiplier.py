#!/usr/bin/env python3
""" Complex types - functions
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a multiplicated function.
    """

    return lambda x: x * multiplier
