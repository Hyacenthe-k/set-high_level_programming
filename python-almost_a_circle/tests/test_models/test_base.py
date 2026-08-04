#!/usr/bin/python3
"""Unittest module for Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class."""

    def test_id_assignment(self):
        """Test auto and explicit ID assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test conversion of dict list to JSON string."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'id': 1, 'width': 10}]
        self.assertEqual(Base.to_json_string(d), '[{"id": 1, "width": 10}]')

    def test_from_json_string(self):
        """Test JSON string conversion to list of dicts."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        s = '[{"id": 1, "width": 10}]'
        self.assertEqual(Base.from_json_string(s), [{'id': 1, 'width': 10}])


if __name__ == "__main__":
    unittest.main()
