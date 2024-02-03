#!/usr/bin/python3
"""
A function that multiplies 2 matrices using the module NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ function body """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists or m_b
                        must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b
                        must be a list of lists")

    if not m_a or not m_b or not all(m_a) or not all(m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(element, (int, float)) for row in m_a
               for element in row):
        raise TypeError("m_a should contain only integers or floats or
                        m_b should contain only integers or floats")

    if not all(isinstance(element, (int, float)) for row in m_b
               for element in row):
        raise TypeError("m_a should contain only integers or floats or
                        m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("Each row of m_a must be of the same
                        size or each row of m_b must be of the same size")

    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("Each row of m_a must be of the same
                        size or each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Convert lists to NumPy arrays and perform matrix multiplication
    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)
    result = np.matmul(np_m_a, np_m_b)

    return result.tolist()
