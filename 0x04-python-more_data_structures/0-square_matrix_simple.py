#!/bin/usr/python3

def square_matrix_simple(matrix=[]):
     # Create a new matrix with the same dimensions as the input matrix
    new_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    # Iterate through the input matrix and square each element
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
