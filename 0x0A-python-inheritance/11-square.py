#!/usr/bin/python3


"""
Module for Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes an instance of the Square class.

        Args:
        - size (int): The size of the square.
        """

        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        Formatted string representing the square.
        """

        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - The area of the square.
        """

        return self.__size ** 2
