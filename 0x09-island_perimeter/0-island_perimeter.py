#!/usr/bin/python3
""" Island Perimeter challenge"""


def island_perimeter(grid):
    """ Function that returns the perimeter
    of the island described in grid
    """
    heigth = len(grid)
    width = len(grid[0])
    x = 0
    y = 0

    for i in range(heigth):
        for j in range(width):
            if grid[i][j] == 1:
                x += 1
                if (j > 0 and grid[i][j - 1]) == 1:
                    y += 1
                if (i > 0 and grid[i - 1][j]) == 1:
                    y += 1
    return x * 4 - y * 2


if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
