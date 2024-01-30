#!/usr/bin/python3
"""A function that adds 2 integers
    Args:
        a, b: first number and second number (b=98)
    Returns:
        int: a + b"""


def add_integer(a, b=98):
    """Args: a, b (int / float) - first and second number(b defaults to 98)
    Raises: TypeError - if a or b are not integers
    Returns: int - the sum of a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
