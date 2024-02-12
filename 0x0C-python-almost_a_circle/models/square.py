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

    def update(self, *args, **kwargs):
        """update body"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ method body """
        attributes = ['id', 'size', 'x', 'y']
        return {key: getattr(self, key) for key in attributes}
