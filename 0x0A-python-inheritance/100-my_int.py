#!/usr/bin/python3
''' MyInt Class module '''


class MyInt(int):
    ''' rebel int inverted equals '''
    def __init__(self, value):
        self._Int__value = value

    def __eq__(self, other):
        ''' equality inverter '''
        if self._Int__value == other:
            return False
        return True

    def __ne__(self, other):
        ''' inequality inverter '''
        return(not self.__eq__(other))
