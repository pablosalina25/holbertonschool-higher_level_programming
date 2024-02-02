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
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """
        Print a square using '#' characters to stdout.

        If the size is 0, it prints an empty line. Otherwise, it prints a square
        with the specified size.

        Each row of the square is printed as a string of '#' characters.
        """
        if self.__size == 0:
            print()
        for j in range(self.__size):
            for colm in range(self.__size):
                print("#", end="")
            print()

