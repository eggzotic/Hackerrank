#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    noAnswer = 'no answer'
    n = len(w)
    if n == 1: return noAnswer
    if n == 2:
        return w[1] + w[0] if w[0] < w[1] else noAnswer
    for i in range(n - 2, -1, -1):
        trailing = w[i:]
        sortedTrailing = ''.join(sorted(trailing))
        betterIndex = bisect_right(sortedTrailing, w[i])
        tailLength = len(trailing)
        if betterIndex < tailLength and betterIndex > 0:
            newW = w[:i] + sortedTrailing[betterIndex]
            sortedTrailing = sortedTrailing[:betterIndex] + sortedTrailing[min(tailLength,betterIndex + 1):]
            return newW + sortedTrailing
    return noAnswer

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
