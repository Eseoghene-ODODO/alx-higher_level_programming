#!/usr/bin/python3
"""
    function definition
    0-add_integer module
    0-add_integer supplies one function, add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """function definition
    TypeError
    return statement"""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
