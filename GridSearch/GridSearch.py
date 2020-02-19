#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.


def gridSearch(G, P):
    # height & width of G
    rG = len(G)
    cG = len(G[0])
    # height & width of P
    rP = len(P)
    cP = len(P[0])
    # effective width to scan
    width = cG - cP + 1
    height = rG - rP + 1
    for i in range(height):
        for j in range(width):
            # if first char matches then dive into a complete comparison
            if G[i][j] == P[0][0]:
                subG = subGrid(G, i, rP, j, cP)
                if areSameGrid(subG, P): return 'YES'
    return 'NO'

def subGrid(grid, rowStart, rows, colStart, cols):
    subRows = grid[rowStart: rowStart + rows]
    return list(map(lambda list: list[colStart: colStart + cols], subRows))

def areSameGrid(g1, g2):
    h = len(g1)
    w = len(g1[0])
    if h != len(g2) or w != len(g2[0]): return False
    for i in range(h):
        if g1[i] != g2[i]: return False
    return True

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
