#!/usr/bin/python3
"""
A function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """ function body """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
