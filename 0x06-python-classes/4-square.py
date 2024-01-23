#!/usr/bin/python3
"""
A Class Square that defines a square
"""


class Square:
    """ class body """

    def __init__(self, size=0):
        """ instance of a class """
        self.__size = size

    @property
    def size(self):
        """ property body """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter body """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ method body """
        return self.__size * self.__size
