#!/usr/bin/python3
"""
Create a function def island_perimeter(grid): that returns
the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in a grid.
    Args:
        grid:  2d list of integers containing 0(water) or i(land)
    Return:
        Ther perimeter of the island
    """

    pmt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    pmt += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    pmt += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    pmt += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    pmt += 1
    return pmt
