#!/usr/bin/python3
"""Module with the Rectable class"""


class Rectangle:
    """Rectangle class with height and width attributes"""
    def __init__(self, width=0, height=0):
        """Initer"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns private attr width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets private attr width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns private attr height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets private attr height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
