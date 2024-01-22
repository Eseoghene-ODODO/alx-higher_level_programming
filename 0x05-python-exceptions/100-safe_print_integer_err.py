#!/usr/bin/python3
"""
A function that prints an integer.
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=open(2, 'w'))
        return False
