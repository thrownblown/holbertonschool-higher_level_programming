#!/usr/bin/python3
class BaseGeometry():
    ''' base class for geo objects '''

    def area(self):
        ''' throws error for future proof '''
        raise Exception("area() is not implemented")
