#!/usr/bin/python3
"""This is pascal triangle module"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    :param n: The number of rows in Pascal's Triangle.
    :type n: int
    :return: A list of lists representing Pascal's Triangle.
    :rtype: List[List[int]]
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
