#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class body """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ instance of a class """
        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width

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

    def __str__(self):
        """ str body """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += "#" * self.__width + "\n"
        return result.rstrip()

    def __repr__(self):
        """repr body """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ del body """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
