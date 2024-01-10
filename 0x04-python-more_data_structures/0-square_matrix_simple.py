#!/usr/bin/python3
"""
A function that computes the square values of all integers of a matrix
"""


def square_matrix_simple(matrix=[]):
    """ function body """
    new_matrix = []
    for rows in matrix:
        new_matrix.append([rows[element] ** 2 for element in range(len(rows))])
    return new_matrix
