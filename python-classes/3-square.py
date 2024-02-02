#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A class Square that defines a square by: (based on 2-square.py)."""


class Square:

    """This is the Square Class"""

    def __init__(self, size=0):
        """Initializing the square size"""

        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Return the area of the square"""

        return self.__size * self.__size

