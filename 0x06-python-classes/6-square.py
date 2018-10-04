#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (len(value) is not 2 or type(value[0]) is not int or type(value[1])
                is not int or value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        pos = self.position
        if self.size > 0:
            for row in range(self.size + pos[1]):
                if row < pos[1]:
                    print()
                else:
                    for col in range(self.size + pos[0]):
                        if col < pos[0]:
                            print(end=' ')
                        else:
                            print('#', end='')
                    print()
        else:
            print()
