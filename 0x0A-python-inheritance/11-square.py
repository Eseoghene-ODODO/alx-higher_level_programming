#!/usr/bin/python3
"""importing 9-rectangle module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initialization of the square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[{Square.__name__}] {self.__size}/{self.__size}"
