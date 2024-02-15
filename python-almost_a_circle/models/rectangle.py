#!/usr/bin/python3
"""
Define the Rectangle class.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class inheriting from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """
        Print the Rectangle instance in stdout using the character '#'.
        """
        for t in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Update the Rectangle attributes based on the given arguments or keyword arguments.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        if "id" in kwargs:
            self.id = kwargs["id"]
        elif "width" in kwargs:
            self.width = kwargs["width"]
        elif "height" in kwargs:
            self.height = kwargs["height"]
        elif "x" in kwargs:
            self.x = kwargs["x"]
        elif "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Return a dictionary representation of the Rectangle.
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
