#!/usr/bin/python3
"""
A function that returns the list of available attributes and
methods of an object
"""


def lookup(obj):
    """ function body """
    return list(dir(obj))
