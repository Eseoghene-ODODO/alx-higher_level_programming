#!/usr/bin/python3
"""
A function that mimics the bytecode
"""


def magic_calculation(a, b):
    result = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except (ValueError, TypeError) as err:
            result += b + a

    return result
