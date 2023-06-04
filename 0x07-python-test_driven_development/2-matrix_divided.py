#!/usr/bin/python3
""" Module matrix_divided
Divides each element of a matrix of numbers by a number
"""


def matrix_divided(matrix, div):
    """Returns a new matrix (list of list)
    with the result of the division of matrix by div
    rounded to 2 decimal places.
    """

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for x in row:
            if not type(x) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
