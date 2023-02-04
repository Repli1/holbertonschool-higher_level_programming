#!/usr/bin/python3
"""Defines a class named Square"""


class Square():
    """Defines a private attribute named size"""
    def __init__(self, size=0):
        self._Square__size = size
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError

    def area(self):
        return self._Square__size**2
