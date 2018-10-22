#!/usr/bin/python3
''' Square Class module '''
from .Rectangle import Rectangle


class Square(Rectangle):
    ''' shape class for 4 sided object with right angles and equal sides '''
    def __init__(self, size):
        self.integer_validator("size", size)
        super(Square, self).__init__(size, size)
