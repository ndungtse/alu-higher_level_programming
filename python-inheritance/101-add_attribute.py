#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to obj if it can have one.

    Args:
        obj: the object to add the attribute to.
        name: the name of the new attribute.
        value: the value of the new attribute.

    Raises:
        TypeError: if obj cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
