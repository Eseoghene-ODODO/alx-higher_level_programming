#!/usr/bin/python3
def add_integer(a, b=98):
    """function that adds two numbers"""
    if not isinstance(a, int) | isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) | isinstance(b, float):
        raise TypeError("b must be an integer")
    elif isinstance(a, float):
        return int(a)
    elif isinstance(b, float):
        return int(b)
    return a + b
