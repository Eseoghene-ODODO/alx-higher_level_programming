#!/usr/bin/python3
"""
A function that replaces or adds key/value in a dictionary
"""


def update_dictionary(a_dictionary, key, value):
    """ Function body """
    if not isinstance(a_dictionary, dict):
        return None
    a_dictionary[key] = value
    return a_dictionary
