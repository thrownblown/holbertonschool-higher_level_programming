#!/usr/bin/python3
""" Square Class module """
from .rectangle import Rectangle


class Square(Rectangle):
    """ shape class for 4 sided obj with and equal sides """
    def __init__(self, size=1, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string descriptor of the rectangle"""
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size
        ))

    def update(self, *args, **kwargs):
        """ updates the rectangle dimensions """
        if len(args):
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ returns a dict with apropos key value pairs """
        return({
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        })
