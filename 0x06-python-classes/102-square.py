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

    def __eq__(self, other):
        """
        Method that overrides the equality operator
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Method that overrides the inequality operator
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Method that overrides the less than operator
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Method that overrides the less than or equal to operator
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Method that overrides the greater than operator
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Method that overrides the greater than or equal to operator
        """
        return self.area() >= other.area()


if "__main__" == __name__:
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
