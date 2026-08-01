#!/usr/bin/python3
"""Defines a function that inserts text after lines containing a string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line of filename containing search_string.

    Args:
        filename: the file to modify.
        search_string: the string to look for in each line.
        new_string: the text to insert after each matching line.
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
