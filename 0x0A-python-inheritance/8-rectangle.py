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
