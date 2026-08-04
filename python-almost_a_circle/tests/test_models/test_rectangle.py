#!/usr/bin/python3
"""Unittest module for Rectangle class."""
import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""

    def test_attributes(self):
        """Test instantiation attributes."""
        r = Rectangle(10, 2, 1, 1, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 5)

    def test_type_errors(self):
        """Test type validation errors."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "1")

    def test_value_errors(self):
        """Test value validation errors."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_to_dictionary(self):
        """Test to_dictionary representation."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), d)

    def test_update_args(self):
        """Test update method with *args."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_create(self):
        """Test create class method."""
        r1 = Rectangle(3, 5, 1, 2, 99)
        d = r1.to_dictionary()
        r2 = Rectangle.create(**d)
        self.assertEqual(str(r2), "[Rectangle] (99) 1/2 - 3/5")

    def test_save_to_file(self):
        """Test save_to_file class method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_from_file(self):
        """Test load_from_file class method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].id, 1)


if __name__ == "__main__":
    unittest.main()
