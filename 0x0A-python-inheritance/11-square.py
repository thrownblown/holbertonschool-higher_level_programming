#!/usr/bin/python3
''' BaseGeometry, Rectangle, and Square Class module '''


class BaseGeometry():
    ''' base class for geo objects '''

    def area(self):
        ''' throws error for future proof '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' makes sure our values are numbers over 0 '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    ''' shape class for 4 sided object with right angles '''
    def __init__(self, width, height):
        ''' validates inputs and sets dimensions '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        return(self.__width * self.__height)

    def __str__(self):
        return ("[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height
        ))


class Square(Rectangle):
    ''' shape class for 4 sided object with right angles and equal sides '''
    def __init__(self, size):
        super(Square, self).__init__(size, size)
        self.size = size
