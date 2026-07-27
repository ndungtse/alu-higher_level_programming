#!/usr/bin/python3
"""Defines a LockedClass that restricts dynamic instance attributes."""


class LockedClass:
    """Only allows the dynamic creation of a 'first_name' attribute."""

    __slots__ = ("first_name")
