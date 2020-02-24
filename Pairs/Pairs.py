#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    n = len(arr)
    pairCount = 0
    for i in range(n - 1):
        plusK = arr[i] + k
        # find the position just past where the required +k element will be, if at all
        index = bisect_right(arr, plusK)
        if index > n: continue
        if arr[index - 1] == plusK:
            pairCount += 1
    return pairCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
