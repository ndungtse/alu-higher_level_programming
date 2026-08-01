#!/usr/bin/python3
"""Defines matrix_divided, dividing every element of a matrix by a number."""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div, rounded to 2 dp.

    matrix must be a list of lists of ints/floats with equal-length rows,
    and div must be a nonzero number.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(err)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(err)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
