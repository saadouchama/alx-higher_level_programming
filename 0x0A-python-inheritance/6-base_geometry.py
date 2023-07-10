#!/usr/bin/python3


"""
Module: BaseGeometry

This module provides the definition for the BaseGeometry class,
which serves as a base class for geometric calculations.

"""


class BaseGeometry:
    """
    BaseGeometry class defines the basic structure for geometric calculations.

    Methods:
    - area(): Raises an exception and should be implemented in derived classes.
    """

    @classmethod
    def area(self):
        """
        Calculates the area of the geometric shape.

        This method is intended to be overridden by derived classes to
        provide the specific implementation for calculating the area of
        the corresponding geometric shape.

        Raises:
        Exception: Always raises an exception when called.
        """
        raise Exception("area() is not implemented")
