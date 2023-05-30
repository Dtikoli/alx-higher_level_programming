#!/usr/bin/python3
"""Define class Square with private attribute size and
public attribute area. Allows for access and updating pf size.
"""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print()
