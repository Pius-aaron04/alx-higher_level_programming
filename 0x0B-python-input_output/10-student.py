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

    def to_json(self, attrs=None):
        """
        return a dictionary of attribuets and values.
        """

        if attrs is None:
            return self.__dict__
        elif type(attrs) is list:
            new_dict = {}
            for name in attrs:
                if name in self.__dict__:
                    new_dict.update({name: self.__dict__.get(name)})
            return new_dict
        else:
            return self.__dict__
