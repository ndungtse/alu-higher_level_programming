#!/usr/bin/python3
"""Defines text_indentation, printing text with breaks after ., ? and :."""


def text_indentation(text):
    """Print text with two newlines after each '.', '?' and ':'.

    Leading and trailing spaces of each printed line are removed, and
    text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
