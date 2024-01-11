#!/usr/bin/python3
"""
A function that returns a set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    """ Function body """
    diff_elements = set()
    for element in set_1:
        if element not in set_2:
            diff_elements.add(element)
    for elem in set_2:
        if elem not in set_1:
            diff_elements.add(elem)
    return diff_elements
