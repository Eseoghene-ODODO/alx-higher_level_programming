#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


class BaseGeometry:
    """ class body """

    def area(self):
        """ method body """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method body """
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = name
        self.value = value


class Rectangle(BaseGeometry):
    """ class body """

    def __init__(self, width, height):
        """ method body """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
