#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """function that computes the square value
    of all integers of a matrix"""
    new_matrix = [[0 for col in range(len(matrix[0]))]
                  for row in range(len(matrix))]

    for k in range(len(matrix)):
        for l in range(len(matrix[0])):
            new_matrix[k][l] = matrix[k][l] ** 2
    return new_matrix
