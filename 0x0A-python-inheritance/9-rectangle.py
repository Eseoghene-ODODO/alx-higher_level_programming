#!/usr/bin/python3
""""imported module from 7-base_geometry.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a Rectangle class that inherits BaseGeometry from 7-base_geometry.py"""

    def __init__(self, width, height):
        """initialization of width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """implementation of area method"""
        return self.__height * self.__width

    def __str__(self):
        """implementation of string method"""
        return f"[{Rectangle.__name__}] {self.__width}/{self.__height}"
