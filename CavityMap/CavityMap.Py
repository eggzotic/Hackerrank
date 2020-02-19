#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.


def cavityMap(grid):
    n = len(grid)
    newGrid = []
    for i in range(n):
        row = grid[i]
        # 1st & last rows are "edges"
        if i == 0 or i == n-1:
            newGrid.append(row)
            continue
        m = len(row)
        for j in range(m):
            # 1st & last col are "sides"
            if j == 0:
                newGrid.append(grid[i][j])
                continue
            if j == m - 1:
                newGrid[i] += grid[i][j]
                continue
            above = grid[i - 1][j]
            below = grid[i + 1][j]
            left = grid[i][j - 1]
            right = grid[i][j + 1]
            here = grid[i][j]
            if here > max(above, below, left, right):
                newGrid[i] += 'X'
            else:
                newGrid[i] += grid[i][j]
    return newGrid


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
