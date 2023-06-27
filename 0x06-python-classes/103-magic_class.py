#!/usr/bin/python3

"""Defines a class MagicClass"""

import math


class MagicClass:
    """This class is the bytecode of a function"""

    def __init__(self, radius=0):
        """Initializes the class
        Args:
            radius (int): radius of the class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the class
        Returns:
            The area of the class
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the class
        Returns:
            The circumference of the class
        """
        return 2 * math.pi * self.__radius
