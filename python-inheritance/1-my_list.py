#!/usr/bin/python3
"""
This module creates a class MyList that inherits from list.
"""


class MyList(list):
    """
    This is a class that defines a list.
    """

    def print_sorted(self):
        """
        This method prints the list in a sorted order.
        """

        print(sorted(self))
