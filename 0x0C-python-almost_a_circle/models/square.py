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
        return self._size

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        self.__size = value
