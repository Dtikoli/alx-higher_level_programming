#!/usr/bin/python3
"""A geometry module that defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize an instance of square.

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)
