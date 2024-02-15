#!/usr/bin/python3

"""Defines a Square class inheriting from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """A Square class inheriting from the Rectangle class"""

    def __init__(self, side_length, x=0, y=0, identifier=None):
        """Initializes the Square."""
        super().__init__(side_length, side_length, x, y, identifier)

    @property
    def side_length(self):
        """Returns the side length of the square."""
        return self.width

    @side_length.setter
    def side_length(self, value):
        """Sets the side length of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates attributes based on arguments."""
        if args:
            self.id, self.side_length, self.x, self.y = (
                args[:4] + (self.y,) * (4 - len(args))
            )
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the square."""
        return {
            "id": self.id,
            "side_length": self.width,
            "x": self.x,
            "y": self.y
        }
