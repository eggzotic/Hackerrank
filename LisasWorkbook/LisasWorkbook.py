#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page = 0
    specialCount = 0
    for probCountPerChapter in arr:
        lastProb = 1
        while probCountPerChapter > 0:
            page += 1
            probs = min(probCountPerChapter, k)
            probCountPerChapter -= probs
            if page in list(range(lastProb, lastProb + probs)): specialCount += 1
            lastProb += probs
    return specialCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
