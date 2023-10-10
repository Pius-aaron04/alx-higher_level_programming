#!/usr/bin/python3
"""
Defines a function that converts python objects to json objects.
"""

import json


def to_json_string(my_obj):
    """
    converts to my_obj to json object.
    """

    return json.dumps(my_obj)
