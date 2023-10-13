#!/usr/bin/python3
"""
contains definition for base class.
"""


class Base:
    """
    Base class for this project.
    """

    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes instance attributes.
        """

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
