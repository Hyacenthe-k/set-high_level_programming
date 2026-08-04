#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
import os
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

    def test_update_args(self):
        """Test update method with positional arguments."""
        s = Square(5, 0, 0, 1)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1)
        self.assertEqual(s.size, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """Test update method with keyword arguments."""
        s = Square(5, 0, 0, 1)
        s.update(id=89)
        self.assertEqual(s.id, 89)
        s.update(id=89, size=1)
        self.assertEqual(s.size, 1)
        s.update(id=89, size=1, x=2)
        self.assertEqual(s.x, 2)
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(s.y, 3)

    def test_create(self):
        """Test create class method for Square."""
        s1 = Square(5, 2, 3, 89)
        d = s1.to_dictionary()
        s2 = Square.create(**d)
        self.assertEqual(str(s2), "[Square] (89) 2/3 - 5")

    def test_save_to_file(self):
        """Test save_to_file for Square."""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        s = Square(1)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file(self):
        """Test load_from_file for Square when file exists/doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])
        s = Square(5, 1, 1, 1)
        Square.save_to_file([s])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].id, 1)


if __name__ == "__main__":
    unittest.main()
