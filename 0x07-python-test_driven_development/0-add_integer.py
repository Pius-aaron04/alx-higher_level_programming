#!/usr/bin/python3
"""
This module contain function definition.
"""


def add_integer(a, b=98):
    """
    this function adds two numbers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    elif type(b) not in (int, float):
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    return int(a) + int(b)
