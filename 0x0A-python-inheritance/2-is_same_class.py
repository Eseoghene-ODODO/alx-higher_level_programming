#!/usr/bin/python3
""""Module for is_same_class"""


def is_same_class(obj, a_class):
    """function that returns True if an object is exactly
       same as the class, otherwise False"""

    return type(obj) is a_class
