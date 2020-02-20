#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    # store the sums in hashes to avoid mass duplicate calculations
    def sumUpTo(i: int):
        if i in sumTo:
            return sumTo[i]
        sumTo[i] = sumTo[i - 1] + arr[i - 1]
        return sumTo[i]
    #
    def sumDownTo(i: int):
        if i >= n: return 0
        if i in sumFrom:
            return sumFrom[i]
        sumFrom[i] = sumFrom[i - 1] - arr[i - 1]
        return sumFrom[i]
    #
    n = len(arr)
    sumTo = {0: 0}
    sumFrom = {0: sum(arr)}
    #
    for i in range(n):
        if sumUpTo(i) == sumDownTo(i + 1): return 'YES'
    return 'NO'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
