#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle construction, validation and behavior."""

    def test_is_base_subclass(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_attributes(self):
        """Constructor assigns width, height, x, y and id."""
        r = Rectangle(10, 20, 3, 4, 7)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (10, 20, 3, 4, 7))

    def test_default_x_y(self):
        """x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_width_type(self):
        """A non-int width raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 2)

    def test_width_value(self):
        """A non-positive width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_type(self):
        """A non-int height raises TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "2")

    def test_height_value(self):
        """A non-positive height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)

    def test_x_type(self):
        """A non-int x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, {})

    def test_x_value(self):
        """A negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 2, -1)

    def test_y_type(self):
        """A non-int y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 0, "0")

    def test_y_value(self):
        """A negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 2, 0, -1)

    def test_bool_rejected(self):
        """A bool width is rejected as a non-integer."""
        with self.assertRaises(TypeError):
            Rectangle(True, 2)

    def test_area(self):
        """area returns width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display_simple(self):
        """display prints the rectangle ignoring x/y when both are 0."""
        with io.StringIO() as buf, redirect_stdout(buf):
            Rectangle(2, 2).display()
            self.assertEqual(buf.getvalue(), "##\n##\n")

    def test_display_with_offsets(self):
        """display honors x and y offsets."""
        with io.StringIO() as buf, redirect_stdout(buf):
            Rectangle(2, 3, 2, 2).display()
            self.assertEqual(buf.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """__str__ follows the [Rectangle] (id) x/y - w/h format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """update assigns positional args in id/w/h/x/y order."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update assigns keyword args by name."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_update_args_precede_kwargs(self):
        """kwargs are ignored when positional args are present."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, width=99)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)

    def test_to_dictionary(self):
        """to_dictionary returns all fields with correct values."""
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(
            r.to_dictionary(),
            {"id": r.id, "width": 10, "height": 2, "x": 1, "y": 9})
        self.assertIs(type(r.to_dictionary()), dict)


if __name__ == "__main__":
    unittest.main()
