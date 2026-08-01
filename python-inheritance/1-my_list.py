#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """A list subclass that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
