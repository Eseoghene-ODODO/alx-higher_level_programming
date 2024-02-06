#!/usr/bin/python3
"""
A class called BaseGeometry
"""


class BaseGeometry:
    """ class body """

    def area(self):
        """ method body """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method body """
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = name
        self.value = value
