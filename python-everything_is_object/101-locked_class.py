#!/usr/bin/python3
"""Module that defines a LockedClass."""


class LockedClass:
    """A class that prevents dynamic creation of attributes

    except if the attribute is named 'first_name'.
    """
    __slots__ = ['first_name']
