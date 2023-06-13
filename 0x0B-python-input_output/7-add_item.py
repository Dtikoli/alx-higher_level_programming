#!/usr/bin/python3
"""A module that adds arguments to a list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        arglist = load_from_json_file("add_item.json")
    except FileNotFoundError:
        arglist = []
    arglist.extend(sys.argv[1:])
    save_to_json_file(arglist, "add_item.json")
