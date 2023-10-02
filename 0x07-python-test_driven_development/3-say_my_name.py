#!/usr/bin/python3
"""
This Module contains a say my name function.
"""


def say_my_name(first_name, last_name=""):
    """
    This functions says your name.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(first_name, last_name)
