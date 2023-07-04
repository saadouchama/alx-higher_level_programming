#!/usr/bin/python3

"""
This module contains a function that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty.
        TypeError: If m_a or m_b contains a non int/float.
        TypeError: If m_a or m_b contains a row of different size.

    Returns:
        list: The result matrix.
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    if len(set([len(row) for row in m_a])) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set([len(row) for row in m_b])) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for col in range(len(m_b[0]))] for row in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
