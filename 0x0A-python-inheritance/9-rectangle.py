#!/usr/binpython3
"""
conatains rectangle class definition.
"""


BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """
    defines Rectangle class (sub class of BaseGeometry).
    """

    def __init__(self, width, height):
        """
        initializes instance attributes.
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns the area of rectangle.
        """

        return self.__height * self.__width

    def __str__(self):
        """
        printable representation of instance.
        """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
