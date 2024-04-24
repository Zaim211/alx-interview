#!/usr/bin/python3
""" Rotate 2D Matrix Challenge """


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90
    degrees clockwise. """
    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix)):
            matrix[row][col], matrix[col][row] = \
                    matrix[col][row], matrix[row][col]

    for rows in matrix:
        rows.reverse()
