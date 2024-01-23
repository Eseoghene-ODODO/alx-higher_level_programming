#!/usr/bin/python3
"""
A Class Square that defines a square
"""


class Square:
    """ class body """

    def __init__(self, size=0):
        """ instance of a class """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
