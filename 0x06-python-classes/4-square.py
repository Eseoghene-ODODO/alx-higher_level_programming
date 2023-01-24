#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """Initialization of a square"""
    def __init__(self, size=0):
        self.__size = size
        
    def size(self):
        return(self.__size)
    
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """function that returns the area of the square"""
        return(self.__size ** 2)
