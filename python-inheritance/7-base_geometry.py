#!/usr/bin/python3
"""
Defines a BaseGeometry class with integer validation functionality.
"""


class BaseGeometry:
    """A base class for geometry objects with integer validation."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer (or is a boolean).
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
