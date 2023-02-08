#!/usr/bin/python3
""""Module for is_kind_of__class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if an object is an instance of or
       if the object is an instance class that inherited from the same
       class, otherwise False"""

    if isinstance(obj, a_class):
        return True
    return False
