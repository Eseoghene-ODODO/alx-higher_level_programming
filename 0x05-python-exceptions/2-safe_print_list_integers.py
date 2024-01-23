#!/usr/bin/python3
"""
A function that prints the first x elements of a list
and only integers
"""


def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            integers_printed += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            raise
    print()
    return integers_printed
