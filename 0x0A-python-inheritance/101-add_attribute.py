#!/usr/bin/python3
"""A module with a function that adds attributes to objects."""


def add_attribute(obj, attr, val):
    """Adds a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        attr (str): The name of the attribute to add to obj.
        val (any): The value of attr.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
