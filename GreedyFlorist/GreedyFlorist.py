#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    n = len(c)
    c.sort()
    c.reverse()
    total = 0
    if n <= k: return sum(c)
    inc = 1
    rounds = n // k
    for i in range(0, rounds):
        for j in range(k):
            total += c[i * k + j] * inc
        inc += 1
    index = rounds * k
    while index < n:
        total += inc * c[index]
        index += 1
    return total

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
