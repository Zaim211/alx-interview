#!/usr/bin/python3
""" Rotate 2D Matrix Challenge """


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90
    degrees clockwise. """
    for elements in range(len(matrix) - 1, -1, -1):
        for element in range(0, len(matrix)):
            matrix[element].append(matrix[elements].pop(0))
