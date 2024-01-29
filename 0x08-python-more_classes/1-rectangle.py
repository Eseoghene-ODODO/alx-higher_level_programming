#!/usr/bin/python3
"""
An empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
        Rectangle body
    """
    def __init__(self, width=0, height=0):
        """ initializing the width and height values """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrieving the width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting the the width value """
        self.__width = value
        if value < 0:
            raise ValueError("width must be >= 0")
        elif type(value) not in [int]:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ retrieving height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting the height value and checking for errors """
        self.__height = value
        if value < 0:
            raise ValueError("height must be >= 0")
        elif type(value) not in [int]:
            raise TypeError("height must be an integer")
