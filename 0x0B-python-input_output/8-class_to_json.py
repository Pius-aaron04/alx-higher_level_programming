#!/usr/bin/python3
"""
Contains a function that returns a dict of an object's attributes.
"""


def class_to_json(obj):
    """
    returns a dict of attributes and their values.
    """

    return obj.__dict__
