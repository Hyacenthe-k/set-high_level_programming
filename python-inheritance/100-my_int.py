#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int with inverted == and != operators.
"""


class MyInt(int):
    """A rebel integer class with == and != operators inverted."""

    def __eq__(self, other):
        """Inverts == operator to return True when not equal."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts != operator to return True when equal."""
        return super().__eq__(other)
