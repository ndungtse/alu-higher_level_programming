#!/usr/bin/python3
"""Defines a MyInt class with inverted == and != operators."""


class MyInt(int):
    """A rebel int whose == and != operators are inverted."""

    def __eq__(self, other):
        """Return True when the values are NOT equal."""
        return int(self) != other

    def __ne__(self, other):
        """Return True when the values ARE equal."""
        return int(self) == other
