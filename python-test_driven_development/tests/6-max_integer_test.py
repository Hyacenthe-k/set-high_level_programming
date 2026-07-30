#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test list with max value at the start."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test list with single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test list with floating point numbers."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_negative_numbers(self):
        """Test list of negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)


if __name__ == '__main__':
    unittest.main()
