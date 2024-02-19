#!/usr/bin/python3
"""
Module: rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.

    Returns:
        None. The matrix is edited in-place.
    """
    n = len(matrix)

    # Traverse layers starting from outermost
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            # Save top element
            top = matrix[first][i]
            # Move left to top
            matrix[first][i] = matrix[last - (i - first)][first]
            # Move bottom to left
            matrix[last - (i - first)][first] = matrix[last][last - (
                i - first)]
            # Move right to bottom
            matrix[last][last - (i - first)] = matrix[i][last]
            # Move top to right
            matrix[i][last] = top
