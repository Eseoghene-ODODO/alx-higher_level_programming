#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """initialization of BaseGeometry"""
    def area(self):
        """public instance method (area)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = value
