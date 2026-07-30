#!/usr/bin/python3
"""
Defines an integer addition function.
"""


def add_integer(a, b=98):
    """Adds two integers or float values casted to integers.

    Args:
        a: First number.
        b: Second number, defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
