#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    h = len(A)
    w = len(A[0])
    # surface area of top & bottom
    sa = h * w * 2
    # surface area of the left-front (& opposite)
    for i in range(h):
        row = A[i]
        sa += max(row) * 2
        sa += valleys(row)
    # surface area of the right-front (& opposite)
    for j in range(w):
        col = list(map(lambda row: A[row][j], range(h)))
        sa += max(col) * 2
        sa += valleys(col)
    return sa

def valleys(row):
    # valleys can occur in a "row" of length at least 3
    if len(row) <= 2: return 0
    # scan for valleys/wells
    fall = 0
    rise = 0
    netChange = 0
    rowLen = len(row)
    falling = False
    rising = False
    for j in range(1,rowLen):
        if row[j - 1] > row[j]:
            falling = True
            if rising:
                localChange = min(rise, fall)
                netChange += localChange * 2
                fall -= localChange
                rising = False
                rise = 0
            fall += row[j - 1] - row[j]
        elif row[j - 1] < row[j]:
            if falling:
                falling = False
                rising = True
            if rising: rise += row[j] - row[j - 1]
    if rising:
        netChange += min(rise, fall) * 2
    return netChange

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
