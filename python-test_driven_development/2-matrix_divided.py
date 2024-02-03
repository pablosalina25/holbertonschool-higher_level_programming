#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides every part of a grid by a number and gives back a new grid.
    """
    error_message = ("matrix must be a matrix (list of lists) "
                     "of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError(error_message)
    for j in matrix:
        if not isinstance(j, list):
            raise TypeError(error_message)
        for element in j:
            if not isinstance(element, (int, float)):
                raise TypeError(error_message)

    common_row_length = len(matrix[0])
    for j in matrix:
        if len(j) != common_row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
 
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for j in matrix:
        new_row = []
        for element in j:
            new_item = round(element / div, 2)
            new_row.append(new_item)
        result_matrix.append(new_row)

    return result_matrix

