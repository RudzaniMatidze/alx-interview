#!/usr/bin/python3
"""
A function that returns a list of integers representing
the Pascal's triangle on n.
"""


def pascal_triangle(n):
    """
    This function generates Pascal's Triangle up to the nth row.

    Args:
        n: An interger representing the number of rows in the triangle.

    Returns:
        A list of lists containing the values of Pascal's Triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    # The first row is always [1]
    triangle.append([1])

    # Iterate for the remaining rows
    for i in range(1, n):
        # Each row starts with 1
        row = [1]
        # Fill the middle elements using the previous row
        for j in range(1, i):
            previous_row = triangle[i - 1]
            row.append(previous_row[j - 1] + previous_row[j])
        # Last element is always 1
        row.append(1)
        triangle.append(row)

    return triangle
