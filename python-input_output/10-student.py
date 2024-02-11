#!/usr/bin/python3
"""In this module, a 'Student' class is defined."""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes_to_include=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        if attributes_to_include is not None and isinstance(attributes_to_include, list):
            dictionary = {}
            for k in attributes_to_include:
                if hasattr(self, k):
                    dictionary[k] = getattr(self, k)
            return dictionary
        else:
            return self.__dict__
