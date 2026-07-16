#!/usr/bin/python3
"""Defines a MagicClass that matches specific bytecode."""

import math


class MagicClass:
    """Represents a circle math utility structure."""

    def __init__(self, radius=0):
        """Initializes a MagicClass.

        Args:
            radius (int or float): The radius of the magic class circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the structure."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the structure."""
        return 2 * math.pi * self.__radius
