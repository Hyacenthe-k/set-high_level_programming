#!/usr/bin/python3
"""Unittest module for Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class."""

    def test_id_auto(self):
        """Test auto incrementing ID."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_custom(self):
        """Test explicit ID assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string(self):
        """Test to_json_string conversion."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        """Test from_json_string conversion."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{'id': 12}])


if __name__ == "__main__":
    unittest.main()
