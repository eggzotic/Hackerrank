#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    # identify all the indices of odd numbers
    oddPosition = {}
    oddCount = 0
    for i in range(len(B)):
        if B[i] % 2 == 1:
            oddCount += 1
            oddPosition[i] = B[i]
    # zero odds means we're done already
    if oddCount == 0: return 0
    # if oddCount is odd, then it's impossible!
    if oddCount % 2 == 1: return 'NO'
    # so oddCount is 2 or more
    # basically we can merge consecutive pairs of odds
    # the "distance" between them, multiply by 2, gives the number of loaves we need to distribute
    oddIndices = sorted(list(oddPosition.keys()))
    distances = 0
    for i in range(1,oddCount,2):
        distances += oddIndices[i] - oddIndices[i - 1]
    return distances * 2

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
