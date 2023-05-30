#!/usr/bin/python3
"""Defines class Square with private attribute size and
public area. Allows for access and update of size.
"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Create a Square
        Args:
            size: length of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """"The propery of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Retrieves the area of a Square
        Returns: The area
        """
        return (self.__size ** 2)

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
