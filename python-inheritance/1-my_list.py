#!/usr/bin/python3
"""
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """A subclass of list with a method to print sorted elements."""

    def print_sorted(self):
        """Prints the list in sorted ascending order without modifying it."""
        print(sorted(self))
