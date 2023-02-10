#!/usr/bin/python3
"""Function that checks if an object inherits from a class"""


def inherits_from(obj, a_class):
    """Returns True or False"""
    return isinstance(obj, a_class) and type(obj) != a_class
