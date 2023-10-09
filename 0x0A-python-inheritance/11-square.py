#!/usr/bin/python3
"""
Contains class definition for square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    defines Square class.
    """

    def __init__(self, size):
        """
        initializes instance attributes.
        """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size


    def __str__(self):
        """
        string representation of instance.
        """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
