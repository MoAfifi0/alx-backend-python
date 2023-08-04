#!/usr/bin/env python3
"""string and int/float
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key and its value to a tuple and return the results
    """

    return (k, float(v**2))
