#!/usr/bin/python3
"""Defines add_integer, a function that adds two integers or floats.

Float arguments are cast to integers before the addition is performed,
and a TypeError is raised when an argument is neither an int nor a float.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    a and b must be integers or floats; floats are cast to int first.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
