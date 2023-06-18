#!/usr/bin/python3
"""A module that defines the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization an instance of Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of square"""
        return f"[Square] ({self.id})self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates the arguments in the class"""
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictonary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
