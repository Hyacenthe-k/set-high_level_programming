#!/usr/bin/python3
"""
Defines a matrix division function.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div rounded to 2 decimal places.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide by.

    Returns:
        A new matrix with divided results.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(val / div, 2) for val in row] for row in matrix]
