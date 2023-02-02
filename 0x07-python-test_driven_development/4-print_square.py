#!/usr/bin/python3
"""function that prints a square with the character #
    arg:
    size
"""


def print_square(size):
    """function body
        Error types:
        TypeError, ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif float(size) < 0:
        raise TypeError("size must be an integer")
    for a in range(size):
        for b in range(size):
            print("#", end="")
        print()
