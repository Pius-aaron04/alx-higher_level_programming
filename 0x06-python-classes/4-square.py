#!/usr/bin/python3
""" This module contains the definition of a Square Class with size."""


class Square:
    """ This is an empty Square Class."""
    def __init__(self, size=0):
        """ Initializes private size attribute for Square ininstance."""

        if type(size) is not int:
            raise TypeError("size must be integer")
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
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        self.__size = size
