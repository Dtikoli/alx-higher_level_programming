#!/usr/bin/python3
"""A module that defines a textfile insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as rfile:
        for line in rfile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wfile:
        wfile.write(text)
