#!/usr/bin/python3
"""
Defines a square printing function.
"""


def print_square(size):
    """Prints a square with the # character.

    Args:
        size: The integer side length of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
