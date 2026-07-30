#!/usr/bin/python3
"""
This module contains the `lazy_matrix_mul` function.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using the module NumPy.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        numpy.ndarray: Result of multiplying m_a and m_b.
    """
    return np.matmul(m_a, m_b)
