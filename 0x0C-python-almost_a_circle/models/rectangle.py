#!/usr/bin/python3
"""A module that defines that Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
        Represents the Rectangle class that inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the vaule of the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width attribute"""
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Gets the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height attribute"""
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Gets the value of the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of the x attribute"""
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Gets thee value of the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of the y attribute"""
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints to stdout a visual display of the rectangle"""
        disp = ""
        print("\n" * self__.y, end="")
        for i in range(self.__height):
            disp += (" " * self__.x) + ("#" * self__.width) + "\n"
        print(disp, end="")

    def update(self, *args, **kwargs):
        """Updates the arguments in the class"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.__id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns a dictionary representation of the class"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    @staticmethod
    def setter_validation(attr, value):
        if type(value) is not int:
            raise TypeError(f"{attr} must be an integer")
        if attr == "x" or attr == "y":
            if value < 0:
                raise ValueError(f"{attr} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attr} must be > 0")

    def __str__(self):
        """Returns the str representation of the class"""
        i = self.__id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return (f"[Rectangle] ({i}) {x}/{y} - {w}/{h}")
