#!/usr/bin/python3
"""A function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file
    and returns the number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
