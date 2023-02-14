#!/usr/bin/python3
"""Reactangle Module that inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """Initialization of the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of the rectangle function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def integer_validator(self, name, value):
        """method to check the attribute type(integer validator)"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be >= 0")
        elif x < 0:
            raise ValueError(f"{name} must be >= 0")
        elif x < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """method to calculate the area of a rectangle"""

        return self.width * self.height

    def display(self):
        """public method: prints in stdout the Rectangle instance
           with the character #"""

        print("\n" * self.y + "\n".join([" " * self.x +
                                         "#" * self.width
                                         for i in range(self.height)]))

    def __str__(self):
        """returns string representation of Rectangle"""

        return f"[{Rectangle.__name__}]({self.id}) {self.x}/{self.y} -\
                {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Public method: assigns an argument to each attribute"""

        attributes = ["id", "width", "height", "x", "y"]
        for attr, arg in zip(attributes, args):
            setattr(self, attr, arg)
        for atr, arg in kwargs.items():
            setattr(self, atr, arg)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        atrributes = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in atrributes}
