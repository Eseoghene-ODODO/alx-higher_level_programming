#!/usr/bin/python3
"""
100-matrix_mul module
100-matrix_mul module supplies one function
"""


def matrix_mul(m_a, m_b):
    """Method that multiplies two matrices
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        matrix: the result
    Raises:
        TypeError: If m_a or m_b are not lists
        TypeError: If m_a or m_b are not lists of lists
        ValueError: If m_a or m_b are empty matrices.
        TypeError: If m_a or m_b contain a non int or float
        TypeError: If m_a or m_b are not rectangular
        ValueError: If m_a or m_b can't be multiplied
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    not_size_a = not_size_b = not_num_a = not_num_b = False

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            not_size_a = 1
        for num in row:
            if type(num) not in (int, float):
                not_num_a = 1

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            not_size_b = 1
        for num in row:
            if type(num) not in (int, float):
                not_num_b = 1

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if not_num_a:
        raise TypeError("m_a should contain only integers or floats")
    if not_num_b:
        raise TypeError("m_b should contain only integers or floats")
    if not_size_a:
        raise TypeError("each row of m_a must be of the same size")
    if not_size_b:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[] for i in range(len(m_a))]

    for row_a in range(len(m_a)):
        for col_b in range(len(m_b[0])):
            c = 0
            for row_b in range(len(m_b)):
                c += m_a[row_a][row_b] * m_b[row_b][col_b]
            result[row_a].append(c)

    return result
