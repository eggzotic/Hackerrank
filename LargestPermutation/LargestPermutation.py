#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    # the array is of length n, with the elements being 1..n, but jumbled
    # build a hash from each element to it's initial index
    positionOf = {}
    n = len(arr)
    for i in range(n):
        positionOf[arr[i]] = i
    i = 0
    swaps = 0
    while i < n and swaps < k:
        t = arr[i]
        if arr[positionOf[n - i]] > t:
            arr[i] = n - i
            arr[positionOf[n - i]] = t
            positionOf[t] = positionOf[n - i]
            positionOf[n - i] = i
            swaps += 1
        i += 1
    return arr

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
