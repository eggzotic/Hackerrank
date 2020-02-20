#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
def nonDivisibleSubset(k, s):
    maxSize = 0
    remainderCount = {}
    #
    for item in s:
        rem = item % k
        if rem in remainderCount:
            remainderCount[rem] += 1
        else:
            remainderCount[rem] = 1
    # manual correction for "remainder 0" - can only count 1 of these
    if 0 in remainderCount: maxSize += 1
    # manual correction for "k is even" - can only count 1 of the remainder-k/2
    if k % 2 == 0:
        halfK = math.floor(k / 2)
        if halfK in remainderCount:
            remainderCount[halfK] = 1
    remCounted = {}
    for rem in remainderCount.keys():
        if rem == 0:
            # maxSize += remainderCount[0]
            continue
        if rem in remCounted: continue
        remCounted[rem] = True
        remCounted[k - rem] = True
        remCount = remainderCount[rem] if rem in remainderCount else 0
        kLessRemCount = remainderCount[k - rem] if k - rem in remainderCount else 0
        maxSize += max(remCount, kLessRemCount)
    return maxSize

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
