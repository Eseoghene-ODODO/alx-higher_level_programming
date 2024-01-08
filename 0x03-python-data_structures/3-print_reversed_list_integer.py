#!/usr/bin/python3
"""
A function that prints all integers in a list in reverse order
"""


def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    for i in new_list:
        print("{}".format(i))
