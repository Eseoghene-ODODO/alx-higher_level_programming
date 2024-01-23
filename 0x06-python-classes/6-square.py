#!/usr/bin/python3
"""
A Class Square that defines a square
"""


class Square:
    """ class body """

    def __init__(self, size=0, position=(0, 0)):
        """ instance of a class """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ property body """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter body """
        self.__position = value
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ method body """
        return self.__size * self.__size

    def my_print(self):
        """ my print body """
        if self.__size == 0:
            print()
        
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
