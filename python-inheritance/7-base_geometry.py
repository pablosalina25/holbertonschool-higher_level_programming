#!/usr/bin/python3
"""Define an empty class BaseGeometry."""


class BaseGeometry:
    """A basic geometric class with empty methods."""
    def area(self):
        """Raise an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if a value is an integer and greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
