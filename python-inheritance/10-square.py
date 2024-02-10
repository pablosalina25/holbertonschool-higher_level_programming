#!/usr/bin/python3
"""Define a class Square that inherits from the Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class inheriting from Rectangle class."""
    def __init__(self, size):
        """Initialize Square class inheriting from Rectangle class."""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square."""
        area = self.__size ** 2
        return area
