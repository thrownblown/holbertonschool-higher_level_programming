#!/usr/bin/python3
"""Module with the Rectable class"""


class Rectangle:
    """Rectangle class with height and width attributes"""
    def __init__(self, width=0, height=0):
        """Initer"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns private attr width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets private attr width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__size = value

    @property
    def height(self):
        """Returns private attr height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets private attr height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns instance area"""
        return(self.width * self.height)

    def perimeter(self):
        """Returns instance perimeter"""
        if self.height is 0 or self.width is 0:
            return(0)
        return(2 * (self.width + self.height))
