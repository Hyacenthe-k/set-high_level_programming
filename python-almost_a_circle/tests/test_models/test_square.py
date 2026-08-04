#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class."""

    def test_attributes(self):
        """Test square instantiation attributes."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_size_setter(self):
        """Test size property setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_to_dictionary(self):
        """Test to_dictionary representation."""
        s = Square(10, 2, 1, 1)
        d = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), d)


if __name__ == "__main__":
    unittest.main()
