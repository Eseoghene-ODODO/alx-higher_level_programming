#!/usr/bin/python3
"""
A function that removes all character c and C from a string
"""


def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
    return new_string
