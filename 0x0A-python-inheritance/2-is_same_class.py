#!/usr/bin/python3

"""
Module for is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class

    Args:
        obj (any): object to check
        a_class (any): class to check against

    Returns:
        bool: True if the object is exactly an instance of the specified class
    """
    return type(obj) == a_class
