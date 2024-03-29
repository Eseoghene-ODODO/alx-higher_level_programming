#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class body """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instance of a class """
        Rectangle.number_of_instances += 1
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

    def __str__(self):
        """ str body """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += str(self.print_symbol) * self.__width + "\n"
        return result.rstrip()

    def __repr__(self):
        """repr body """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ del body """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method body """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
