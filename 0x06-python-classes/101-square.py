#!/usr/bin/python3
""" This module contains the definition of a Square Class with size."""


class Square:
    """ This is an empty Square Class."""
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes private size attribute for Square ininstance."""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        self.__size = size

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(x) is not int for x in position) or any(x < 0 for x in
                                                              position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    def my_print(self):
        """ Prints instance image."""

        if self.size == 0:
            print()
            return
        if self.position[1] > 1:
            if self.position[1] % 2 == 0:
                y1 = self.position[1] // 2
                y2 = y1
            else:
                y1 = (self.position[1] // 2) + 1
                y2 = y1 - 1
        else:
            y1 = self.position[1]
            y2 = 0
        for k in range(y1):
            print()
        for i in range(self.size):
            print(' ' * self.position[0], end='')
            for j in range(self.size):
                print('#', end='')
            print()
        for k in range(y2):
            print()

    @property
    def position(self):
        """ gets the position attribute of instance."""

        return self.__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(x < 0 for x in position) or any(type(x) is not int for x in
                                                 position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def __repr__(self) -> str:
        """
        string representation of Square instance.
        """

        rep = ""
        if self.size == 0:
            return rep
        if self.position[1] > 1:
            if self.position[1] % 2 == 0:
                y1 = self.position[1] // 2
                y2 = y1
            else:
                y1 = (self.position[1] // 2) + 1
                y2 = y1 - 1
        else:
            y1 = self.position[1]
            y2 = 0
        for k in range(y1):
            rep += '\n'
        for i in range(self.size):
            rep += ' ' * self.position[0]
            for j in range(self.size):
                rep += '#'
            rep += '\n'
        for k in range(y2):
            rep += '\n'
        return rep[:-1]
