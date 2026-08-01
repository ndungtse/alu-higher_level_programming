#!/usr/bin/python3
"""Defines a function returning the JSON-serializable dict of an object."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of obj.

    All attributes of obj are assumed to be serializable: list, dictionary,
    string, integer and boolean.
    """
    return obj.__dict__
