#!/usr/bin/python3
"""
A class Square that inherits from Rectangle(9-rectangle.py)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class body """

    def __init__(self, size):
        """ method body """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ method body """
        return self.__size ** 2

    def _str__(self):
        """method body """
        return f"[Square.__name__] {self.__size}/{self.__size}"
