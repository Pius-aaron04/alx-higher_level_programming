#!/usr/bin/python3
"""
Class definition for class Student'
"""


class Student:
    """
    Defines Student class.
    """

    def __init__(self, first_name, last_name, age):
        """
        intializes object attributes.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return a dictionary of attribuets and values.
        """

        return self.__dict__
