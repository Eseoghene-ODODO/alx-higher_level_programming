#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class body """
    def __init__(self, width=0, height=0):
        """ instance of a class """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ property body """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter body """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ property body """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter body """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ area body """
        return self.__height * self.__width

    def perimeter(self):
        """ perimeter body """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
