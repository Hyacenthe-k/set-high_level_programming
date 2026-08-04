#!/usr/bin/python3
"""Unittest module for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""

    def test_creation_and_attributes(self):
        """Test initialization and getters/setters."""
        r = Rectangle(10, 2, 1, 1, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 99)

    def test_invalid_types(self):
        """Test type validation."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "1")

    def test_invalid_values(self):
        """Test value validation."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_to_dictionary(self):
        """Test dictionary representation."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), d)


if __name__ == "__main__":
    unittest.main()
