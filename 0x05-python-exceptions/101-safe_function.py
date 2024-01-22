#!/usr/bin/python3
import sys
"""
A function that executes a function safely
"""


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
