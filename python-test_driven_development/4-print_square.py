#!/usr/bin/python3
"""Defines print_square, which prints a square made of the # character."""


def print_square(size):
    """Print a square of side length size using the # character.

    size must be an integer greater than or equal to 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
