#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # Q's distance to left, down, right, up
    dL = c_q - 1
    dD = r_q - 1
    dR = n - c_q
    dU = n - r_q
    # Q's attack-able squares (without obstacles): up, up-right, right, down-right, down, down-left, left, up-left
    aU = dU
    aUR = min(dU, dR)
    aR = dR
    aDR = min(dR, dD)
    aD = dD
    aDL = min(dD, dL)
    aL = dL
    aUL = min(dL, dU)
    #
    # Now identify the obstacles in the attack-path
    oL  = list(filter(lambda cell: cell[0] == r_q and cell[1] < c_q, obstacles))
    oUL = list(filter(lambda cell: cell[0] - r_q == c_q - cell[1] and cell[0] > r_q and cell[1] < c_q, obstacles))
    oU  = list(filter(lambda cell: cell[1] == c_q and cell[0] > r_q, obstacles))
    oUR = list(filter(lambda cell: cell[0] - r_q == cell[1] - c_q and cell[0] > r_q and cell[1] > c_q, obstacles))
    oR  = list(filter(lambda cell: cell[0] == r_q and cell[1] > c_q, obstacles))
    oDR = list(filter(lambda cell: r_q - cell[0] == cell[1] - c_q and cell[0] < r_q and cell[1] > c_q, obstacles))
    oD  = list(filter(lambda cell: cell[1] == c_q and cell[0] < r_q, obstacles))
    oDL = list(filter(lambda cell: r_q - cell[0] == c_q - cell[1] and cell[0] < r_q and cell[1] < c_q, obstacles))
    # update the attach-paths for the obstacles
    if len(oL) > 0:
        aL = c_q - max(map(lambda cell: cell[1], oL)) - 1
    if len(oU) > 0:
        aU = min(map(lambda cell: cell[0], oU)) - r_q - 1
    if len(oR) > 0:
        aR = min(map(lambda cell: cell[1], oR)) - c_q - 1
    if len(oD) > 0:
        aD = r_q - max(map(lambda cell: cell[0], oD)) - 1
    if len(oUR) > 0:
        aUR = min(map(lambda cell: cell[0], oUR)) - r_q - 1
    if len(oDR) > 0:
        aDR = r_q - max(map(lambda cell: cell[0], oDR)) - 1
    if len(oDL) > 0:
        aDL = r_q - max(map(lambda cell: cell[0], oDL)) - 1
    if len(oUL) > 0:
        aUL = min(map(lambda cell: cell[0], oUL)) - r_q - 1
    aTotal = sum([aU,aUR,aR,aDR,aD,aDL,aL,aUL])
    return aTotal

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
