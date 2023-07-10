#!/usr/bin/python3


"""
Module for Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes an instance of the Rectangle class.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        - The area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        Formatted string representing the rectangle.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
