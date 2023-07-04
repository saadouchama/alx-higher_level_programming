#!/usr/bin/python3

"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """This function prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Returns:
        None

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
