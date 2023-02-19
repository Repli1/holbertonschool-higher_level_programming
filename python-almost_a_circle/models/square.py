#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Private and public attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        string = f"[Square] ({self.id}) {self.x}/{self.y}"
        string += f" - {self.width}"
        return string

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Attribute updater"""
        attributes = ["id", "size", "x", "y"]
        i = 0
        if args and len(args) > 0:
            for element in args:
                setattr(self, attributes[i], element)
                i += 1
        elif kwargs:
            for element in kwargs:
                setattr(self, element, kwargs[element])

