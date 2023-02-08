#!/usr/bin/python3
"""Defines a class named Square"""


class Square():
    """Defines a private attribute named size"""
    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        self._Square__position = position

    @property
    def size(self):
        return self._Square__size

    @property
    def position(self):
        return self._Square__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self._Square__size = value

    @position.setter
    def position(self, array):
        if type(array) is tuple and len(array) == 2:
            pass
        else:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        self._Square__position = array

    def area(self):
        return self._Square__size**2

    def my_print(self):
        for l in range(0, self._Square__position[1]):
            print("")
        for j in range(0, self._Square__size):
            for k in range (0, self._Square__position[0]):
                print(" ", end="")
            for i in range(1, self._Square__size):
                print("#", end="")
            print("#")
        if self._Square__size == 0:
            print("")
