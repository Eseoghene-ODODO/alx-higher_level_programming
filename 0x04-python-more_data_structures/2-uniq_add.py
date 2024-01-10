#!/usr/bin/python3
"""
A function that adds all unique integers in a list(only once for each integers)
"""


def uniq_add(my_list=[]):
    """ Function body """
    uniq_set = set()
    result = 0
    for element in my_list:
        if element not in uniq_set:
            result += element
            uniq_set.add(element)
    return result
