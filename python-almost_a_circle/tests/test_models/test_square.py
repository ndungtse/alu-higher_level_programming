#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import unittest
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square construction, validation and behavior."""

    def test_is_rectangle_subclass(self):
        """Square inherits from Rectangle."""
        self.assertIsInstance(Square(1), Rectangle)

    def test_size_sets_width_and_height(self):
        """size is used for both width and height."""
        s = Square(5)
        self.assertEqual((s.width, s.height, s.size), (5, 5, 5))

    def test_attributes(self):
        """Constructor assigns size, x, y and id."""
        s = Square(3, 1, 3, 7)
        self.assertEqual((s.size, s.x, s.y, s.id), (3, 1, 3, 7))

    def test_size_type(self):
        """A non-int size raises TypeError with the width message."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("9")

    def test_size_value(self):
        """A non-positive size raises ValueError with the width message."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_setter(self):
        """The size setter updates width and height together."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_validation(self):
        """The size setter validates like width."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_area(self):
        """area returns size squared."""
        self.assertEqual(Square(5).area(), 25)

    def test_display(self):
        """display honors x and y offsets."""
        with io.StringIO() as buf, redirect_stdout(buf):
            Square(2, 2).display()
            self.assertEqual(buf.getvalue(), "  ##\n  ##\n")

    def test_str(self):
        """__str__ follows the [Square] (id) x/y - size format."""
        s = Square(3, 1, 3, 12)
        self.assertEqual(str(s), "[Square] (12) 1/3 - 3")

    def test_update_args(self):
        """update assigns positional args in id/size/x/y order."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """update assigns keyword args by name."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_to_dictionary(self):
        """to_dictionary returns id, size, x and y."""
        s = Square(10, 2, 1)
        self.assertEqual(
            s.to_dictionary(),
            {"id": s.id, "size": 10, "x": 2, "y": 1})
        self.assertIs(type(s.to_dictionary()), dict)


if __name__ == "__main__":
    unittest.main()
