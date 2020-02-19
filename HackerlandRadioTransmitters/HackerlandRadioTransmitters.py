#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    xmitters = 0
    x.sort()
    i = x[0]
    n = len(x)
    # create a set for faster membership
    xSet = set(x)
    while True:
        j = k
        while j > 0:
            if i + j in xSet:
                i += j
                xmitters += 1
                break
            j -= 1
        if j == 0: xmitters += 1
        i += k + 1
        if i > x[n - 1]: break
        # find the next actual house
        while i not in xSet: i += 1
    return xmitters

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
