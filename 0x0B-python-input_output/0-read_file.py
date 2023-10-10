#!/usr/bin/python3
"""
Contains definition of functions that reads a file.
"""


def read_file(filename=""):
    """
    Opens file and prins content to stdout.
    """

    with open(filename, "r", encoding='utf-8') as file_:
        print(file_.read(), end="")
