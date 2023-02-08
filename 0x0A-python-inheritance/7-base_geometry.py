#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """initialization of BaseGeometry"""

    def area(self):
        """public instance method (area)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method to validate value is an int"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
