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

        self.validate_value('width', width)
        self.validate_value('height', height)
        self.validate_value('x', x)
        self.validate_value('y', y)
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

        super().validate_value('width', width)
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

        self.validate_value('height', height)
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

        self.validate_value('x', x)
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

        self.validate_value('y', y)
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

    def update(self, *args, **kwargs):
        """
        updates instances attributes.
        """

        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                return
        else:
            for key, value in kwargs.items():
                if key != 'id':
                    s_key = '_Rectangle__' + key
                else:
                    s_key = key
                if s_key in self.__dict__:
                    self.validate_value(key, value)
                    setattr(self, s_key, value)

    def to_dictionary(self):
        """
        returns a dictionary representation of instance
        """

        dict_ = {'id': self.id, 'width': self.width,
                 'height': self.height, 'x': self.x, 'y': self.y}

        return dict_
