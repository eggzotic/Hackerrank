#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    squareCount = 0
    # find the first square >= a
    n = math.ceil(math.sqrt(a))
    square =  n * n
    if square > b: return 0
    # find the difference between consecutive squares:
    #  (n + 1)^2 - n^2 == n^2 + 2n + 1 - n^2 == 2n + 1
    # so to hop from square-to-square we can just increment by 2n + 1
    while square <= b:
        squareCount += 1
        square += 2 * n + 1
        n += 1
    return squareCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
