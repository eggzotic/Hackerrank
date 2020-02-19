#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def twoPluses(grid):
    rows = len(grid)
    cols = len(grid[0])
    #
    bigPlus = {}
    # scan the grid to find the largest "+" possible centered on each cell
    for i in range(rows):
        for j in range(cols):
            bigPlus[cellName(i, j)] = plusCells(i,j,grid)
    best = 0
    for iCell in bigPlus.keys():
        iPlus = bigPlus[iCell]
        for jCell in bigPlus.keys():
            if iCell == jCell: continue
            jPlus = bigPlus[jCell]
            while (overlapping(iPlus, jPlus)):
                if len(iPlus) > len(jPlus):
                    iPlus = trimPlus(iPlus)
                else:
                    jPlus = trimPlus(jPlus)
            product = len(iPlus) * len(jPlus)
            if product > best: best = product
            iPlus = bigPlus[iCell]
    return best

def overlapping(plus: list, other: list):
    # empty cells cannot overlap
    if len(plus) == 0 or len(other) == 0: return False
    # first element is the "center" cell of the plus
    # centers are the same - we're checking a plus against itself
    if plus[0] == other[0]: return False
    # now for the main check
    return len(set(plus) & set(other)) > 0

def trimPlus(plus: list):
    # plus will be a list of cells, including the center-cell
    # take the length, subtract 1, divide-by 4 --> the length of each side
    # the sides will be ordered: center-cell, above, below, left, right
    sideLength = math.floor((len(plus) - 1) / 4)
    # if nothing left to remove but the center itself!
    if sideLength == 0: return []
    # remove the last cell from each side
    center = plus[0]
    above = plus[1: sideLength]
    below = plus[sideLength + 1 : sideLength * 2]
    left = plus[sideLength * 2 + 1 : sideLength * 3]
    right = plus[sideLength * 3 + 1: sideLength * 4]
    # and reassemble the lists for the newly trimmed "+"
    return [center, *above, *below, *left, *right]

def cellName(i: int, j: int):
    return f'{i}+{j}'

def plusCells(i: int, j: int, grid):
    bigG = 'G'
    rows = len(grid)
    cols = len(grid[0])
    # store the 4 legs in these
    above = []
    below = []
    left = []
    right = []

    # cells on edges - can not have any legs
    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1: return [cellName(i, j)]

    # above
    for y in range(1,i + 1):
        if grid[i - y][j] != bigG: break
        above.append(cellName(i-y,j))
    # below
    for y in range(i + 1, rows):
        if grid[y][j] != bigG: break
        below.append(cellName(y,j))
    # to-the left
    for x in range(1, j + 1):
        if grid[i][j - x] != bigG: break
        left.append(cellName(i,j-x))
    # to-the right
    for x in range(j + 1, cols):
        if grid[i][x] != bigG: break
        right.append(cellName(i, x))
    # trim all down to the max-common length
    sideLength = min(len(above), len(below), len(left), len(right))
    above = above[:sideLength]
    below = below[:sideLength]
    left = left[:sideLength]
    right = right[:sideLength]
    # combine in this order to store the plus
    return [cellName(i, j), *above, *below, *left, *right]

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
