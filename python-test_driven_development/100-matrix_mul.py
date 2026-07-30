#!/usr/bin/python3
"""
Defines a matrix multiplication function.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        New matrix containing the product of m_a and m_b.
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

    if not all(isinstance(val, (int, float)) for row in m_a for val in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for row_a in m_a:
        new_row = []
        for col_idx in range(len(m_b[0])):
            elem_sum = 0
            for row_idx in range(len(m_b)):
                elem_sum += row_a[row_idx] * m_b[row_idx][col_idx]
            new_row.append(elem_sum)
        new_matrix.append(new_row)

    return new_matrix
