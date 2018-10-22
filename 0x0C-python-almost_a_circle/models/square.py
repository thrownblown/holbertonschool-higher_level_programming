#!/usr/bin/python3
""" Square Class module """
from .rectangle import Rectangle


class Square(Rectangle):
    """ shape class for 4 sided obj with and equal sides """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        self.size = value

    def __str__(self):
        """Returns a string descriptor of the rectangle"""
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size
        ))
