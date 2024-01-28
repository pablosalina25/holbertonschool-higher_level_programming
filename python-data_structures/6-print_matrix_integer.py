#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for j in range(0, len(line)):
            print("{:d}".format(line[j]), end=' ' if j < len(line) - 1 else '')
        print()
