#!/usr/bin/python3
"""A file IO module that defines a textfile reading function."""


def read_file(filename=""):
    """Prints the read content of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
