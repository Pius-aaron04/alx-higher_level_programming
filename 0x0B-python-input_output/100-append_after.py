#!/usr/bin/python3
"""
Contains function definition that appends text to a file after
a specified string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    appends `new_string` to file `filename` after search_string is found.
    """

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, "w", encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
