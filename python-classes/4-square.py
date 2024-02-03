#!/usr/bin/python3
"""A class Square that defines a square by: (based on 2-square.py)."""


class Square:
    """This is the Square Class"""

    def __init__(self, size=0):
        """Initializing the square size"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
