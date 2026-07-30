#!/usr/bin/python3
"""
Defines a matrix multiplication function using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        Product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
