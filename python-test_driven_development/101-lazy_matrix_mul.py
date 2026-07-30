#!/usr/bin/python3
"""Module that provides a lazy function to multiply two matrices."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices, delegating the multiplication to NumPy.

    Args:
        m_a (list): first matrix, a list of lists of ints/floats.
        m_b (list): second matrix, a list of lists of ints/floats.

    Returns:
        numpy.ndarray: the matrix product of m_a and m_b.

    Raises:
        TypeError: if m_a or m_b is not a list, not a list of lists,
            contains non integer/float values, or rows are not all
            of the same size.
        ValueError: if m_a or m_b is empty.
        Exception: whatever NumPy itself raises if m_a and m_b
            can't be multiplied together.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)) or isinstance(elem, bool):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)) or isinstance(elem, bool):
                raise TypeError("m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    return np.matmul(m_a, m_b)
