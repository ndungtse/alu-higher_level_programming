#!/usr/bin/python3
"""Defines lazy_matrix_mul, which multiplies two matrices using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the matrix product of m_a and m_b computed with numpy.matmul."""
    return np.matmul(m_a, m_b)
