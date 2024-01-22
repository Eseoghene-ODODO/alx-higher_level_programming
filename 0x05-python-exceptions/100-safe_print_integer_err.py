#!/usr/bin/python3
import sys
"""
A function that prints an integer.
"""


def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
