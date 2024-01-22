#!/usr/bin/python3
"""
A function that divides 2 integers and prints the result
"""


def safe_print_division(a, b):
    """ function body """

    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
    return result
