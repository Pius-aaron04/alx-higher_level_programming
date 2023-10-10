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

        if type(first_name) is not str:
            raise TypeError('first_name must be string')
        if type(last_name) is not str:
            raise TypeError('last_name must be a string')
        if type(age) is not int:
            raise TypeError('age must be an integer')
        elif age < 0:
            raise TypeError('age must be a positive integer')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return a dictionary of attribuets and values.
        """

        return self.__dict__
