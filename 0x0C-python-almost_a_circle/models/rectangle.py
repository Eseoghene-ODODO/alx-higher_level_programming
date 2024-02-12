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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        return self.width * self.height

    def display(self):
        """method body"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """method body"""
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """update method"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """method body"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        return {key: getattr(self, key) for key in attributes}
