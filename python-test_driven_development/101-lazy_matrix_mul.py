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
        TypeError: If m_a or m_b are not lists or lists of lists.
        ValueError: If m_a or m_b are empty or cannot be multiplied.
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
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    len_a = len(m_a[0])
    for row in m_a:
        if len(row) != len_a:
            raise TypeError("each row of m_a must be of the same size")

    len_b = len(m_b[0])
    for row in m_b:
        if len(row) != len_b:
            raise TypeError("each row of m_b must be of the same size")

    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
