#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    sortedArr = sorted(arr)
    n = len(sortedArr)
    minDiff = -1
    minPairs = []
    for i in range(1, n):
        diff = sortedArr[i] - sortedArr[i - 1]
        if minDiff == -1 or diff < minDiff:
            minDiff = diff
            minPairs = []
            minPairs.append(sortedArr[i - 1])
            minPairs.append(sortedArr[i])
        elif diff == minDiff:
            minPairs.append(sortedArr[i - 1])
            minPairs.append(sortedArr[i])
    return minPairs

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
