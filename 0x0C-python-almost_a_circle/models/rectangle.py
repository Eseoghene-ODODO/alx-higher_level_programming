#!/usr/bin/python3
"""
A Rectangle class that inherits from the Base class
"""

from models.base import Base


class Rectangle(Base):
    """class body"""
    __nb_objects = 0
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """method body"""
        super().__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = Rectangle.__nb_objects

    @property
    def width(self):
        """property body"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter body"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property body"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter body"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError("height must be  > 0")
        self.__height = value

    @property
    def x(self):
        """property body"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter body"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """property body"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter body"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError(f'y must be >= 0')
        self.__y = value

    def area(self):
        """area body"""
        return self.__width * self.__height

    def display(self):
        """method body"""
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """method body"""
        return f'[Rectangle] ({self.__id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'
