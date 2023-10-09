#!/usr/bin/python3
"""
Contains a function definition.
"""


def inherits_from(obj, a_class):
    """
    tells if `obj` is a subclass of `a_class`
    """

    return issubclass(type(obj), a_class) or isinstance(obj, a_class)
