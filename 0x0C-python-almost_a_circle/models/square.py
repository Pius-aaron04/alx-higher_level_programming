#!/usr/bin/python3
"""
This contains Square class definition.
"""


import models.rectangle
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes class attributes.
        """

        super().validate_value('size', size)
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns string rep for object
        """

        string = '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                   self.width)

        return string

    @property
    def size(self):
        """
        gets Square instance size
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        sets size value.
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates instance atributes
        """

        if args:
            try:
                for name, value in zip(('id', 'width', 'height', 'x', 'y'), args):
                    super().validate_value(name, value)
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        else:
            for key, value in kwargs.items():
                attribute = '_Rectangle__' + key
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                else:
                    self.validate_value(key, value)
                    setattr(self, attribute, value)

    def to_dictionary(self):
        """
        returns a dictionary reprsentation of instance
        """

        dict_ = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

        return(dict_)
