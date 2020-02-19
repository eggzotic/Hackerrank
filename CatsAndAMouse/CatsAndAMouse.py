#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    catA = 'Cat A'
    catB = 'Cat B'
    mouseC = 'Mouse C'
    #
    distanceA = abs(x - z)
    distanceB = abs(y - z)
    if distanceA == distanceB: return mouseC
    if distanceA < distanceB: return catA
    return catB

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
