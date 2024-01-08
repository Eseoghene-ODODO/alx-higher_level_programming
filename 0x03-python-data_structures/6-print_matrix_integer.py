#!/usr/bin/python3
"""
A function that prints a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    for rows in matrix:
        for i, element in enumerate(rows):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(element), end='')
        print()
