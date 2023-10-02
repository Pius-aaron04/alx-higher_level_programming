#!/usr/bin/python3
"""
This module contains a Rectangle class definition.
"""


class Rectangle:
    """
    This defines a Rectangle class.
    """

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """
        retrieves instance's height attribute.
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets or updates instance's height attribute.
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        retrieves instance's width attribute
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        sets or updates instance's width attribute.
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def area(self):
        """
        gets the area of rectangle instance.
        """

        return self.height * self.width

    def perimeter(self):
        """
        gets the perimeter of rectangle.
        """

        if width == 0 or height == 0:
            return 0
        return (self.width + self.height) * 2
