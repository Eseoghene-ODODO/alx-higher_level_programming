#!/usr/bin/python3
"""
A function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ function body """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not (m_a or all(m_a)):
        raise ValueError("m_a can't be empty")

    if not (m_b or all(m_b)):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(element, (int, float))
               for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(element, (int, float))
               for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b))
              for col_b in zip(*m_b)] for row_a in m_a]

    return result
