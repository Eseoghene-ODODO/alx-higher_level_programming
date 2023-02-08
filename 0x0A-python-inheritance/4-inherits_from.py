#!/usr/bin/python3
""""Module for inherits_from"""


def inherits_from(obj, a_class):
    """function that returns True if an object inherits
       (directly or indirectly)
       from the specified class, otherwise False"""

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
