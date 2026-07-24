#!/usr/bin/python3
"""
Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
