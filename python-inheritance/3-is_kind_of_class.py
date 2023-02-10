#!/usr/bin/python3
"""Function that checks if an object is an instance,
   or inherits from a class"""


def is_kind_of_class(obj, a_class):
    """Returns True or False"""
    return isinstance(obj, a_class)
