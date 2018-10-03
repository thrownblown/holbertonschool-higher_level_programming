#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError('size must be >= 0')
        elif type(value) is not int:
            raise TypeError('size must be an integer')
        self.__size = value

        def my_print(self):
            if self.size > 0:
                for col in range(self.size):
                    for row in range(self.size):
                        print('#', end='')
                    print()
            else:
                print()
