#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Represent a base geometry."""

    def area(self):
        """Raise an Exception with a message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a valid integer.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
