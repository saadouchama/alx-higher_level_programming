#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """
    Class that defines a square
    Attributes:
        size (int): size of the square
    """

    def __init__(self, size=0):
        """
        Init method is a constructor for Square class
        Args:
            size: size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Public instance method that returns the current square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Public instance method that returns the current square size
        Args:
            value: size of the square
        Returns:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public instance method that returns the current square area
        """
        return self.__size ** 2
