#!/usr/bin/python3
"""
A function that prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    """ Function body """
    if not isinstance(a_dictionary, dict):
        return None
    sorted_dict = dict(sorted(a_dictionary.items()))
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
