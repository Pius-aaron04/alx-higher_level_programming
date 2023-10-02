#!/usr/bin/python3
"""
This module contains a Rectangle class definition.
"""


class Rectangle:
    """
    This defines a Rectangle class.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        initializes instance attributes.
        """

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
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares two instances based on their sizes.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectange")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

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

        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        returns string representation of instance
        """

        if self.width == 0 or self.height == 0:
            return ""

        string = ""
        for row in range(self.height):
            string += (str(self.print_symbol) * self.width)
            if row != self.height - 1:
                string += '\n'

        return string

    def __repr__(self):
        """
        returns string representation of instance
        """

        string = "Rectangle({}, {})".format(self.width, self.height)

        return string

    def __del__(self):
        """
        detects deletion of instance.
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
