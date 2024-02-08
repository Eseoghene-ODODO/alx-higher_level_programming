#!/usr/bin/python3
"""
A class Student that defines a student
"""


class Student:
    """class body"""

    def __init__(self, first_name, last_name, age):
        """method body"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method body"""
        return self.__dict__

    def to_json(self, attrs=None):
        """ method body """
        if attrs is None:
            return self.__dict__
        return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
                }
