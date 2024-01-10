#!/usr/bin/python3
"""
A function that returns a set of common elements in two sets
"""


def common_elements(set_1, set_2):
    """ Function body """
    common_set = set()
    for element in set_1:
        if element in set_2:
            common_set.add(element)
    return common_set
