#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

        a (int or float): First integer.
        b (int or float): Second integer (default is 98).

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

