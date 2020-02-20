#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    pos = 0
    moves = 0
    while True:
        if pos + 2 <= n - 1 and c[pos + 2] == 1:
            pos += 1
        else:
            pos += 2
        moves += 1
        if pos >= n - 1: break
    return moves

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
