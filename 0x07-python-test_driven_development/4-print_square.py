#!/usr/bin/python3
"""
This module contains a function that print square
"""


def print_square(size):
    """
    this function prints a square of specified size
    """

    if type(size) not in (int, float):
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        print('#' * int(size))
