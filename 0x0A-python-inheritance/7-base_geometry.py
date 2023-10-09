#!/usr/bin/python3
"""
Contains a class Geometry class definiton.
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
