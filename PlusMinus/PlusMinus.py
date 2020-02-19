#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    negCount = 0
    posCount = 0
    zeroCount = 0
    n = len(arr)
    for i in arr:
        if i > 0: posCount += 1
        if i < 0: negCount += 1
        if i == 0: zeroCount += 1
    posCount /= n
    negCount /= n
    zeroCount /= n
    print("{0:.6f}".format(posCount))
    print("{0:.6f}".format(negCount))
    print("{0:.6f}".format(zeroCount))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
