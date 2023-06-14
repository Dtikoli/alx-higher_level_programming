#!/usr/bin/python3
"""A module that defines a JSON deserializing function."""
import json


def from_json_string(my_str):
    """Returns python object of a JSON string representation."""
    return json.loads(my_str)
