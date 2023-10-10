#!/usr/bin/python3
"""
Contains a function definition to convert string to json object.
"""

import json


def from_json_string(my_str):
    """
    Converts string to json object.
    """

    return json.loads(my_str)
