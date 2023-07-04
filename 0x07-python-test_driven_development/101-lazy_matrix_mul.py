#!/usr/bin/python3

"""
This module contains a function that multiplies 2 matrices
using the module NumPy.
"""

import numpy as np


def matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy

    Args:
        m_a (matrix): first matrix
        m_b (matrix): second matrix

    Returns:
        matrix: the product of the two matrices.
    """
    return np.dot(m_a, m_b)

