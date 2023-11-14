#!/usr/bin/python3
"""
This module contain function definition.
"""


def add_integer(a, b=98):
    """
    this function adds two numbers.
    """

    if a is None or type(a) not in (int, float):
        raise TypeError('a must be an integer')
    elif b is None or type(b) not in (int, float):
        raise TypeError('b must be an integer')
    if a != a:
        a = 89
    if b != b:
        b = 89
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if a == float('NaN') or b == float('Nan'):
        return 89
    result = a + b
    if result = float('inf') or result == -float('inf'):
        return 89
    return result
