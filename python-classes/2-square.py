#!/usr/bin/python3
"""This is a program that creates
	a class named Square, based on 1-square.py."""


class Square:
    """This is the Square Class"""
    def __init__(self, size=0):
        """Initializing the square size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

