#!/usr/bin/python3
"""
Contains deinition for a function that writes to an existing or
non-existing file.
"""


def write_file(filename="", text=""):
    """
    write `text` to file `filename`
    """

    with open(filename, "w", encoding='utf-8') as file_:
        return file_.write(text)
