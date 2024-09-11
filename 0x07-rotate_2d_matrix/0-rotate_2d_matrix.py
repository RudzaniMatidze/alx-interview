#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """ Transpose the matrix (swap rows with columns)
    Args:
        matrix (list([[list]]): a matrix
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            # Current number
            top = matrix[i][j]
            # Change top for left
            matrix[i][j] = matrix[x][i]
            # Change left for bottom
            matrix[x][i] = matrix[y][x]
            # Change bottom for right
            matrix[y][x] = matrix[j][y]
            # Change right for top
            matrix[j][y] = top
