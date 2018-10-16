#!/usr/bin/python3
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
