#!/usr/bin/python3
"""
A class Square that inherits from a Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class body"""

    def __init__(self, size, x=0, y=0, id=None):
        """method body"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method body"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """property body"""
        return self.width

    @size.setter
    def size(self, value):
        """setter body"""
        self.width = value
        self.height = value
