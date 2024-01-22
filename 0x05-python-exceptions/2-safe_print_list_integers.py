#!/usr/bin/python3
"""
A function that prints the first x elements of a list
and only integers
"""


def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                integers_printed += 1
        print()
    except IndexError as err:
        print(err)
    return integers_printed
