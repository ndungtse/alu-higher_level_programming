#!/usr/bin/python3
"""Defines a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of ints representing Pascal's triangle of n.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)
    return triangle
