#!/usr/bin/python3
"""Module with the Rectangle class"""
from .base import Base


class Rectangle(Base):
    """Rectangle class with height and width attributes"""
    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initer"""
        super(Rectangle, self).__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    @property
    def x(self):
        """Returns private attr x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets private attr x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Returns private attr y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets private attr y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns instance area"""
        return(self.width * self.height)

    def perimeter(self):
        """Returns instance perimeter"""
        if self.height is 0 or self.width is 0:
            return(0)
        return(2 * (self.width + self.height))

    def __display_string(self):
        """Returns str of # with instance dimensions"""
        rect = ''
        if self.height is 0 or self.width is 0:
            return(rect)
        for row in range(self.height + self.y):
            if row >= self.y:
                for col in range(self.width + self.x):
                    if col >= self.x:
                        rect += self.print_symbol
                    else:
                        rect += " "
                if row != (self.height + self.y - 1):
                    rect += '\n'
            else:
                rect += "\n"
        return(rect)

    def __str__(self):
        """Returns a string descriptor of the rectangle"""
        return ("[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        ))

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def display(self):
        """prints a rectangle to the screen"""
        print(self.__display_string())

    def update(self, *args, **kwargs):
        """ updates the rectangle dimensions """
        if len(args):
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
