#!/usr/bin/python3
"""A module that defines the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization an instance of Square"""
        self.setter_validation("size, value)
	super().__init__(size, size, x, y, id)
	self.size = size

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        self.setter_validation("size, value)
        self.__size = value
        self.__width = value
        self.__height = value

    def __str__(self):
        """String representation of square"""
        return f"[Square] ({self.id})self.x}/{self.y} - {self.size}"

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
        """returns dictonary representation of square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
