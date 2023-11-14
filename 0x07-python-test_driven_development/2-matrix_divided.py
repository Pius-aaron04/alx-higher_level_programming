#!/usr/bin/python3
"""
This module Contain a function definition for dividing a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides the individual elements in matrix by div
    """

    result = []

    if type(div) not in (float, int):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or any(type(obj) is not list for obj in
                                       matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        + "integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same "
                            + "size")
        if any(type(x) not in (int, float) for x in matrix[i]):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            + "integers/floats")
        result.append([round(num / div, 2) for num in matrix[i]])

    return result
