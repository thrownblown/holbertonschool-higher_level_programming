#!/usr/bin/python3
"""Module with the Rectable class"""


class Rectangle:
    """Rectangle class with height and width attributes"""
    def __init__(self, width=0, height=0):
        """Initer"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    number_of_instances = 0
    print_symbol = '#'

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

    def area(self):
        """Returns instance area"""
        return(self.width * self.height)

    def perimeter(self):
        """Returns instance perimeter"""
        if self.height is 0 or self.width is 0:
            return(0)
        return(2 * (self.width + self.height))

    def __str__(self):
        """Returns str of # with instance dimensions"""
        rect = ''
        if self.height is 0 or self.width is 0:
            return(rect)
        for row in range(self.height):
            for col in range(self.width):
                rect += str(self.print_symbol)
            if row != self.height - 1:
                rect += '\n'
        return(rect)

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Prints epitaph for del rect"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the greater of two rects by area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)
