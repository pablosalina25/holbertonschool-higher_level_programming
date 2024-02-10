#!/usr/bin/python3
"""Define an empty class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculate and return the area of the rectangle."""
        area = self.__height * self.__width
        return area
    
    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
