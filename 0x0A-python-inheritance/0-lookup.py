#!/usr/bin/python3
"""Defines an object attributes and methods lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes and methods."""
    return (dir(obj))
