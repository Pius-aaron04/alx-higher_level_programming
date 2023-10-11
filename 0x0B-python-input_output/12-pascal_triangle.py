#!/usr/bin/python3
"""
Contains function defintion for pascal traingle.
"""


def pascal_triangle(n):
    """
    returns a 2-D of pascal triangle coeff.
    """

    if n <= 0:
        return []
    triangle = [[1 for k in range(i)] for i in range(1, n + 1)]
    # creates a triangle of 1s
    for i, exp in enumerate(triangle):
        if i < 2:  # skips the first lists in triangle
            continue
        # iterates through each list
        for j in range(len(exp)):
            if j == 0 or j == len(exp) - 1:
                continue
            triangle[i][j] = triangle[i-1][j] + triangle[i - 1][j-1]
    return triangle
