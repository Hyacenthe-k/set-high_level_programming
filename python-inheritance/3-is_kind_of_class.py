#!/usr/bin/python3
"""
Defines a function that checks if an object is an instance of,
or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance or inherited instance of a_class."""
    return isinstance(obj, a_class)
