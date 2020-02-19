#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
willExplodeAt = {}
def bomberMan(n, grid):
    # second 1 - no change - return initial state
    if n == 1: return grid
    # convert the initial locations to a dict
    rows = len(grid)
    cols = len(grid[0])
    # this dict will contain cells neighboring the initial bomb-placements
    #  the values will be:
    #   1 --> "pure" neighbors - having only initial-bomb and other in-range neighbors
    #   0 --> "mixed" neighbors - having "other" neighbors as  well
    neighbors = {}
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                willExplodeAt[cellName(i, j)] = 3
            else:
                willExplodeAt[cellName(i, j)] = 0
    # identify all those "In-range" of an initial bomb
    for i in range(rows):
        for j in range(cols):
            if willExplodeAt[cellName(i, j)] == 0: continue
            above = cellName(i - 1, j)
            if i > 0 and willExplodeAt[above] == 0: neighbors[above] = 1
            below = cellName(i + 1, j)
            if i < rows - 1 and willExplodeAt[below] == 0: neighbors[below] = 1
            right = cellName(i, j + 1)
            if j < cols - 1 and willExplodeAt[right] == 0: neighbors[right] = 1
            left = cellName(i, j - 1)
            if j > 0 and willExplodeAt[left] == 0: neighbors[left] = 1
    # scan the in-range set to determine whether they are neighbors with "other"
    for cell in neighbors.keys():
        (i, j) = cellLocation(cell)
        if i > 0:
            above = cellName(i - 1, j)
            if willExplodeAt[above] == 0 and above not in neighbors:
                neighbors[cell] = 0
                continue
        if i < rows - 1:
            below = cellName(i + 1, j)
            if willExplodeAt[below] == 0 and below not in neighbors:
                neighbors[cell] = 0
                continue
        if j < cols - 1:
            right = cellName(i, j + 1)
            if willExplodeAt[right] == 0 and right not in neighbors:
                neighbors[cell] = 0
                continue
        if j > 0:
            left = cellName(i, j - 1)
            if willExplodeAt[left] == 0 and left not in neighbors:
                neighbors[cell] = 0
                continue

    # direct approach
    for cell in willExplodeAt.keys():
        # seems to be 3 types of cells:
        # 1. those initially populated with a bomb
        # 2. those in-range of those above (and not adjacent to an "other")
        # 3. like 2 above, except also neighboring "others" (below)
        # 3. others (those not initially in-range of bombs)
        #
        if cell in neighbors.keys():
            # type 3 - must go 1st
            if neighbors[cell] == 0:
                willExplodeAt[cell] = 1 if n % 2 == 0 else 0
            # type 2 - next
            else:
                willExplodeAt[cell] = 0 if n % 4 == 3 else 1
            continue
        # type 1 - and these next
        if willExplodeAt[cell] > 0:
            willExplodeAt[cell] = 0 if n % 4 == 3 else 1
            continue
        # type 4
        if willExplodeAt[cell] == 0:
            # applies to cells not initially in-range of a bomb
            willExplodeAt[cell] = 0 if n % 4 == 1 else 1
    return gridState(rows,cols)

def cellName(i, j): return f'{i}+{j}'
def cellLocation(cell: str):
    indexStrings = cell.split('+')
    return [int(indexStrings[0]),int(indexStrings[1])]

def gridState(rows,cols):
    result = []
    for i in range(rows):
        row = ''
        for j in range(cols):
            row += 'O' if willExplodeAt[cellName(i,j)] > 0 else '.'
        result.append(row)
    return result

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
