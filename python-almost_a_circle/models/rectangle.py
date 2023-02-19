#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Private and public attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area"""
        return self.__height * self.__width

    def display(self):
        """Displays rectangle"""
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            string = self.__x * " " + self.__width * "#" + '\n'
            print('\n' * self.__y + string * self.__height, end="")

    def __str__(self):
        string2 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        string2 += f" - {self.__width}/{self.__height}"
        return string2

    def update(self, *args, **kwargs):
        """Attribute updater"""
        attributes = ["id", "width", "height", "x", "y"]
        i = 0
        if args and len(args) > 0:
            for element in args:
                setattr(self, attributes[i], element)
                i += 1
        elif kwargs:
            for element in kwargs:
                setattr(self, element, kwargs[element])

    def to_dictionary(self):
        """Dictionary representation"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
