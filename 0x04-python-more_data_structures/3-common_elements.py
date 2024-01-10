#!/usr/bin/python3
"""
A function that returns a set of common elements in two sets
"""


def common_elements(set_1, set_2):
    """ Function body """
    for element in set_1:
        if element in set_2:
            return element
