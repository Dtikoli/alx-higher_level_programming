#!/usr/bin/python3
"""A module that defines a class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary represntation with a simple data structure."""
    return obj.__dict__
