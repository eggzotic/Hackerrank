#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    # use a hash to store the index of each element of a
    # use a list-value to hold those indices
    # any list with 2 or more values - calculate those distances
    # and finally take the minimum across all those differences
    aHash = {}
    maxDistance = 9999
    minDistance = maxDistance
    for i in range(len(a)):
        if a[i] in aHash:
            aHash[a[i]].append(i)
        else:
            aHash[a[i]] = [i]
    for ai in aHash.keys():
        if len(aHash[ai]) < 2: continue
        for j in range(1, len(aHash[ai])):
            dist = abs(aHash[ai][j] - aHash[ai][j-1])
            if dist < minDistance:
                minDistance = dist
    return -1 if minDistance == maxDistance else minDistance

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
