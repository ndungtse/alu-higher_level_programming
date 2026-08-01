#!/usr/bin/python3
"""Defines say_my_name, which prints a full name from its parts."""


def say_my_name(first_name, last_name=""):
    """Print "My name is <first_name> <last_name>".

    Both first_name and last_name must be strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
