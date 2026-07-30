#!/usr/bin/python3
"""Module that provides a lazy function to multiply two matrices."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a: first matrix, a list of lists of ints/floats.
        m_b: second matrix, a list of lists of ints/floats.

    Returns:
        numpy.ndarray: the matrix product of m_a and m_b.

    Raises:
        Exception: any exception NumPy itself raises when the
            given inputs are invalid or can't be multiplied
            (e.g. TypeError or ValueError from NumPy internals).
    """
    return np.matmul(m_a, m_b)
