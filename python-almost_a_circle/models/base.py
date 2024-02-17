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
            self.id = Base.__nb_object

class MyClass:
    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves objects to a JSON file."""
        dictionary_list = []
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                list_objs = []
            for obj in list_objs:
                dictionary_list.append(obj.to_dictionary())
            file.write(cls.to_json_string(dictionary_list))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries."""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance based on a dictionary."""
        if cls.__name__ == "Rectangle":
            rectangle_instance = cls(3, 13)
            rectangle_instance.update(**dictionary)
            return rectangle_instance
        else:
            square_instance = cls(3)
            square_instance.update(**dictionary)
            return square_instance

    @classmethod
    def load_from_file(cls):
        """Loads instances from a JSON file."""
        if not exists(f"{cls.__name__}.json"):
            return []
        else:
            with open(f"{cls.__name__}.json", "r") as file:
                string = file.read()
                dictionaries = cls.from_json_string(string)
                return [cls.create(**instance_dict)
                        for instance_dict in dictionaries]
