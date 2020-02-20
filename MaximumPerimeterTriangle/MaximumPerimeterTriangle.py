#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    # arrange the sticks in descending order
    sticks.sort()
    sticks.reverse()
    n = len(sticks)
    # then, starting with the largest (first) stick, the next 2 sticks need
    #  to sum to more than it, and move along until we find this combo
    #  or it's a fail
    for i in range(n-2):
        longest = sticks[i]
        mid = sticks[i + 1]
        shortest = sticks[i + 2]
        if mid + shortest > longest:
            return [shortest, mid, longest]
    return [-1]

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
