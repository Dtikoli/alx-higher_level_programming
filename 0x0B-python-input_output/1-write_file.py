#!/usr/bin/python3
"""A file IO module that defines a file writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 textfile.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
