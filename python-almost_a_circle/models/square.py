#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Private and public attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        string = f"[Square] ({self.id}) {self.x}/{self.y}"
        string += f" - {self.size}"
        return string

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size
