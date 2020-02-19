#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    n = len(grid)
    m = len(grid[0])
    sortedGrid = []
    for i in range(n):
        sortedGrid.append(sorted(grid[i]))
    # check the vertical sorted-ness
    for i in range(m):
        col = list(map(lambda x: x[i], sortedGrid))
        for j in range(1,n):
            if col[j - 1] > col[j]: return 'NO'
    return 'YES'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
