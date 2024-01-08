#!/usr/bin/python3
"""
A function that prints all integers in a list in reverse order
"""


def print_reversed_list_integer(my_list=[]):
    for i in reversed(range(len(my_list))):
        print("{:d}".format(my_list[i]))
