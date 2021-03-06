#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    n = len(arr)
    arr.sort()
    minDiff = pow(10,9) + 1
    for i in range(k - 1, n):
        diff = arr[i] - arr[i - k + 1]
        if diff < minDiff: minDiff = diff
    return minDiff

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
