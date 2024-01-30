#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for line in new_matrix:
        for j in range(len(line)):
            line[j] = line[j] * line[j]
    return new_matrix
