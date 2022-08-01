#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class
    Args:
        obj (any): the object to check.
        a_class (type): class criteria to match obj type to.
    Returns:
        Bool
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
