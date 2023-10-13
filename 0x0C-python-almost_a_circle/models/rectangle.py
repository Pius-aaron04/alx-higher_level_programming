#!/usr/bin/python3
"""
contains definition for Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Defines recangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        intializes instance varaibles.
        """

        if type(width) is not int:
            raise TypeError("width must be an intger")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        super().__init__(id)

    @property
    def width(self):
        """
        gets width.
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        sets width.
        """

        if type(width) is not int:
            raise TypeError("width must be an intger")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        gets height.
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        sets height.
        """

        if type(height) is not int:
            raise TypeError("height must be an intger")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        gets x.
        """

        return self.__x

    @x.setter
    def x(self, x):
        """
        sets x ordinate
        """

        if type(x) is not int:
            raise TypeError("x must be an intger")
        elif x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """
        gets y.
        """

        return self.__y

    @y.setter
    def y(self, y):
        """
        sets y ordinate
        """

        if type(y) is not int:
            raise TypeError("y must be an intger")
        elif y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """
        returns the area of a rectangle object.
        """

        return self.width * self.height

    def display(self):
        """
        Displays rectangle object inform 
        of '#' accoreding to its size(width, height).
        """

        if self.y:
            print("\n" * self.y, end='')
        for row in range(self.height):
            if self.x:
                print(' ' * self.x, end='')
                print('#' * self.width)
            else:
                print("#" * self.width)

    def __str__(self):
        """
        String representation of object.
        """

        string = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                         self.y, self.width,
                                                         self.height)
        return string
