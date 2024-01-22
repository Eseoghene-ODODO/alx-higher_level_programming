#!/usr/bin/python3
"""
A function that prints x number of elements
"""


def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for i in my_list[:x]:
            print(i, end="")
            elements_printed += 1
        print()
    except IndexError:
        pass
    return elements_printed
