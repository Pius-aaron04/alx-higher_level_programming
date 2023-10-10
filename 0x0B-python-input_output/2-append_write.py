#!/usr/bin/python3
"""
Contains a definition of a function that qppends to a file.
"""


def append_write(filename="", text=""):
    """
    Appends to a file.
    """

    with open(filename, "a", encoding='utf-8') as file_:
        return file_.write(text)
