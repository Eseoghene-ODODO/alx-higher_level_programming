#!/usr/bin/python3
"""
A function that replaces an element of a list at specific position
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return mylist
    my_list[idx] = element
    return my_list
