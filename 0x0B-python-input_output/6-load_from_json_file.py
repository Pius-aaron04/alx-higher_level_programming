#!/usr/bin/python3
"""
Contains a function creates a json object from a json file.
"""

import json


def load_from_json_file(filename):
    """
    creates json object from file `filename`.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
