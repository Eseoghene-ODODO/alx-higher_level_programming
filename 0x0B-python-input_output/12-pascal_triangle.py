#!/usr/bin/python3
"""
A function that returns a list of list of integers representing the pascal's
triangle of n
"""


def pascal_triangle(n):
    """function body"""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i-1]
        for j in range(1, i):
            row.append(prev_row[j] + prev_row[j-1])
        row.append(1)
        triangle.append(row)
    return triangle
