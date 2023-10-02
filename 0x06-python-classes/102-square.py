#!/usr/bin/python3
""" This module contains the definition of a Square Class with size."""


class Square:
    """ This is an empty Square Class."""
    def __init__(self, size=0):
        """ Initializes private size attribute for Square ininstance."""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        self.__size = size

    def area(self):
        """ Calculates the area of the Square instance."""

        return self.__size ** 2

    @property
    def size(self):
        """ gets the size attribue of the instance"""

        return self.__size

    @size.setter
    def size(self, size):
        """ Sets or updates the size attribute """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        self.__size = size

    def __eq__(self, other):
        """Does th equal comaparison"""
        return self == other

    def __lt__(self, other):
        """Does the less than comaparison"""
        return eval(self) < eval(other)

    def __le__(self, other):
        """Does the less than or equal comaparison"""
        return self <= other

    def __gt__(self, other):
        """Does the greater than comaparison"""
        return self > other

    def __ge__(self, other):
        """Does the great than and equal to"""
        return self >= other

    def __repr__(self):
        """ String rep of instance """
        return "{}".format(self.area)
