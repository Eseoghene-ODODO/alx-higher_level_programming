#!/usr/bin/python3
def add_integer(a, b=98):
    """function that adds two numbers"""
    if not isinstance(a, int) | isinstance(a, float):
        """if statement to check if a is either not an int or float"""
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) | isinstance(b, float):
        """if statement to check if b is either not an int or float"""
        raise TypeError("b must be an integer")
    """return statement to convert a and b to an integer"""
    return int(a) + int(b)
