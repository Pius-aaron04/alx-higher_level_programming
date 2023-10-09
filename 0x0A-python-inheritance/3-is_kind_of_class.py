#!/usr/bin/python3
"""
Contains a function definition.
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is a relative to a_class.
    """

    if (type(obj) is a_class or isinstance(obj, a_class)):
        return True
    return False
