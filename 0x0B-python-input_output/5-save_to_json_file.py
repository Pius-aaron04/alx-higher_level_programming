#!/usr/bin/python3
"""
Contains function definitions that dumps json object into a file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    saves json object `my_obj` into filename.
    """

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
