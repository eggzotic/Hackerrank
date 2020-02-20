#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import repeat

# Complete the matrixRotation function below.
ringContentAt = {}
ringWidthAt = {}
ringHeightAt = {}
#
def matrixRotation(matrix: list, r):
    matrixToRings(matrix)
    for i in ringContentAt.keys():
        rotateRing(i, r)
    matrix = ringsToMatrix()
    for i in range(len(matrix)):
        print(' '.join(map(lambda x: f'{x}', matrix[i])))

def ringsToMatrix():
    # transform back into a matrix
    n = ringHeightAt[0]
    m = ringWidthAt[0]
    # create a matrix of the original size, but initially all positions 0
    matrix = []
    for row in range(n):
        matrix.append(list(repeat(0, m)))
    # walk around the rings, placing the vallues back into their respective
    #  positions (i.e. overwriting the 0's)
    for i in range(len(ringContentAt.keys())):
        height = ringHeightAt[i]
        width = ringWidthAt[i]
        row = i
        col = i
        ringIndex = 0
        # top
        for x in range(width):
            matrix[row][col + x] = ringContentAt[i][ringIndex]
            ringIndex += 1
        # right
        for y in range(1, height):
            matrix[row + y][col + x] = ringContentAt[i][ringIndex]
            ringIndex += 1
        # bottom
        for x in range(width - 2, -1, -1):
            matrix[row + y][col + x] = ringContentAt[i][ringIndex]
            ringIndex += 1
        # left
        for y in range(height - 2, 0, -1):
            matrix[row + y][col + x] = ringContentAt[i][ringIndex]
            ringIndex += 1
    return matrix

def matrixToRings(matrix):
    n = len(matrix)
    m = len(matrix[0])
    # transform matrix into a hash of "rings",
    #  stripping the content from the original matrix as we go
    ringCount = math.ceil(min(n, m) / 2)
    for i in range(ringCount):
        ringHeightAt[i] = len(matrix)
        ringWidthAt[i] = len(matrix[0])
        # top row
        ringContentAt[i] = matrix.pop(0)
        # right-side col
        for j in range(len(matrix)):
            ringContentAt[i].append(matrix[j].pop())
        # bottom row
        bottomRow = list(reversed(matrix.pop()))
        for item in bottomRow:
            ringContentAt[i].append(item)
        # left-side col
        for j in range(len(matrix) - 1, -1, -1):
            ringContentAt[i].append(matrix[j].pop(0))

def rotateRing(index: int, rotationSteps: int):
    ringContent = ringContentAt[index]
    ringLength = 2 * ringWidthAt[index] + 2 * ringHeightAt[index] - 4
    effectiveSteps = rotationSteps % ringLength
    newContent = []
    for i in range(ringLength):
        newContent.append(ringContent[(i + effectiveSteps) % ringLength])
    ringContentAt[index] = newContent

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
