#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """Initialization of the square"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
