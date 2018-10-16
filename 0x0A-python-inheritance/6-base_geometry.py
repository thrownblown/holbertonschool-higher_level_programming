#!/usr/bin/python3
''' BaseGeometry Class module '''


class BaseGeometry():
    ''' base class for geo objects '''

    def area(self):
        ''' throws error for future proof '''
        raise Exception("area() is not implemented")
