#!/usr/bin/python3


"""
Module for inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited from the
    specified class

    Args:
        obj (any): object to check
        a_class (any): class to check against

    Returns:
        bool: True if the object is an instance of a class that inherited from
        the specified class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
