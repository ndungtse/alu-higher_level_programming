#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """A max at the end of an ascending list is found."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """A max in the middle of an unordered list is found."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """A max at the start of the list is found."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """The only element of a one-item list is the max."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Calling with no argument returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """The largest (closest to zero) negative number is found."""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_floats(self):
        """The max of a list of floats is found."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """The max of mixed ints and floats is found."""
        self.assertEqual(max_integer([1, 2, 3.5]), 3.5)

    def test_duplicates(self):
        """A list of equal values returns that value."""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_strings(self):
        """The lexicographically largest string is found."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")


if __name__ == "__main__":
    unittest.main()
