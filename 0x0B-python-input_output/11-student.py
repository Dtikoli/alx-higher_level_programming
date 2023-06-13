#!/usr/bin/python3
"""A module that defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize an instance of Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.

        If attrs is a list of strings, retrieve only attributes
        names included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(mem) == str for mem in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
