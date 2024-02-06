#!/usr/bin/python3
"""
A function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr_name, attr_value):
    """ function body """
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__') and attr_name in obj.__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
