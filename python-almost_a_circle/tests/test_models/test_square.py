#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class."""

    def test_creation(self):
        """Test initialization and attributes."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_size_setter(self):
        """Test size getter and setter validation."""
        s = Square(5)
        s.size = 8
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)
        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_to_dictionary(self):
        """Test dictionary representation."""
        s = Square(10, 2, 1, 1)
        d = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), d)


if __name__ == "__main__":
    unittest.main()
