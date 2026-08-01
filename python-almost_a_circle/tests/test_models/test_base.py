#!/usr/bin/python3
"""Unittests for the Base class."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base id handling and (de)serialization helpers."""

    def tearDown(self):
        """Remove any files created by serialization tests."""
        for name in ("Rectangle.json", "Square.json",
                     "Rectangle.csv", "Square.csv", "Base.json"):
            try:
                os.remove(name)
            except IOError:
                pass

    def test_auto_id_increments(self):
        """Two consecutive auto ids differ by one."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """A provided id is stored as-is."""
        self.assertEqual(Base(12).id, 12)

    def test_id_zero(self):
        """An id of 0 is kept (not treated as None)."""
        self.assertEqual(Base(0).id, 0)

    def test_to_json_string_none(self):
        """None becomes the empty-list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """An empty list becomes the empty-list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_value(self):
        """A list of dicts becomes an equivalent JSON string."""
        d = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        s = Base.to_json_string(d)
        self.assertIs(type(s), str)
        self.assertEqual(json.loads(s), d)

    def test_from_json_string_none(self):
        """None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """An empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_value(self):
        """A JSON string returns the equivalent list of dicts."""
        s = '[{"id": 1, "width": 2}]'
        self.assertEqual(Base.from_json_string(s), [{"id": 1, "width": 2}])

    def test_save_to_file_none(self):
        """Saving None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_objects(self):
        """Saved objects round-trip through their dictionaries."""
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json") as file:
            self.assertEqual(json.loads(file.read()), [r.to_dictionary()])

    def test_create_returns_new_instance(self):
        """create builds an equal but distinct instance."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_load_from_file_missing(self):
        """Loading a missing file returns an empty list."""
        try:
            os.remove("Square.json")
        except IOError:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_roundtrip(self):
        """Loaded instances match the saved ones."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        loaded = Rectangle.load_from_file()
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertIsInstance(loaded[0], Rectangle)

    def test_csv_roundtrip_rectangle(self):
        """Rectangle CSV serialization round-trips."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file_csv([r1])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(str(loaded[0]), str(r1))

    def test_csv_roundtrip_square(self):
        """Square CSV serialization round-trips."""
        s1 = Square(5, 1, 2, 3)
        Square.save_to_file_csv([s1])
        loaded = Square.load_from_file_csv()
        self.assertEqual(str(loaded[0]), str(s1))


if __name__ == "__main__":
    unittest.main()
