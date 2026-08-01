#!/usr/bin/python3
"""Defines a lookup function that lists an object's attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
