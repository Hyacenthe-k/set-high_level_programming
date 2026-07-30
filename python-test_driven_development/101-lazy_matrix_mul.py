#!/usr/bin/python3
"""Module that provides a lazy function to multiply two matrices."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a: first matrix.
        m_b: second matrix.

    Returns:
        numpy.ndarray: the matrix product of m_a and m_b.

    Raises:
        Exception: whatever exception NumPy itself raises when the
            given inputs are invalid or can't be multiplied together.
    """
    return np.matmul(m_a, m_b)
