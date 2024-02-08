#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height attributes.
"""


class Rectangle:
    """
    This class represents a rectangle with width and height attributes.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with a given width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height) if self.width and self.height else 0

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to recreate a new instance using eval().
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
