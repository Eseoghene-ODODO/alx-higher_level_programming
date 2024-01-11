#!/usr/bin/python3
"""
A function that returns a key with the biggest integer value
"""


def best_score(a_dictionary):
    """ Function body """
    if not a_dictionary:
        return None
    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key
