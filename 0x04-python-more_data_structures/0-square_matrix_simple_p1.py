#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for row in new_matrix:
        for idx, element in enumerate(row):
            row[idx] = element**2
    return new_matrix
