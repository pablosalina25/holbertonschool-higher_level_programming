#!/usr/bin/python3
"""Check if the object is an instance of a class inherited from the specified class."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a subclass."""
    return isinstance(obj, a_class) and type(obj) is not a_class
