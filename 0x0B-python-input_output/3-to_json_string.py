#!/usr/bin/python3
"""A module that defines a JSON serializing function."""
import json


def to_json_string(my_obj):
    """Returns the JSON string representation of an object."""
    return json.dumps(my_obj)
