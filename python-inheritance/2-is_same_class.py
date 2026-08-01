#!/usr/bin/python3
"""Defines a function checking exact class membership."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False."""
    return type(obj) is a_class
