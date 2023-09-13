#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Square Matrix function
    Args
    matrix: 2D list

    return values:
    squared values of matrix
    """
    if not matrix:
        return matrix
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, row)))

    return new_matrix
