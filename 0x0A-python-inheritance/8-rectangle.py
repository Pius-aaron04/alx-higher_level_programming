#!/usr/binpython3
"""
conatains rectangle class definition.
"""


class BaseGeometry:
    """
    Geometry Class.
    """

    def area(self):
        """
        area of a figure (yet to be implemented).
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates `value` as an intger.
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
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
