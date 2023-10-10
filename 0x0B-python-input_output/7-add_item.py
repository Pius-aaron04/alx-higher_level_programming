#!/usr/bin/python3
"""
contains function definitions and importations to load and manipulate json
objects.
"""

import json
import sys


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

data = []
try:
    data = load("add_item.json")
    for arg in args:
        data.append(arg)
except Exception:
    with open("add_item.json", "w", encoding='utf-8') as f:
        for arg in args:
            data.append(arg)
finally:
    save(data, 'add_item.json')
