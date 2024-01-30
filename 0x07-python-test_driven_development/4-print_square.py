#!/usr/bin/python3
"""
A function that a square with the character #
"""


def print_square(size):
    """ function body """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
