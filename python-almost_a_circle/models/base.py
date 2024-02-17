#!/usr/bin/python3
"""Write the first Class Base"""
import json
import turtle
from os.path import exists


class Base:
    """A Base Class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """A Function that Initializes the class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries."""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes."""
        if cls.__name__ == "Rectangle":
            Rectangle_two = cls(3, 13)
            Rectangle_two.update(**dictionary)
            return Rectangle_two
        else:
            Square_two = cls(3)
            Square_two.update(**dictionary)
            return Square_two
