#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    n = len(A)
    bCount = {}
    for i in range(n):
        if B[i] in bCount:
            bCount[B[i]] += 1
        else:
            bCount[B[i]] = 1
    for i in range(n):
        if A[i] > k:
            minB = min(B)
            bCount[minB] -= 1
            if bCount[minB] == 0: del(bCount[minB])
            continue
        diff = k - A[i]
        maxB = max(bCount.keys())
        while diff not in bCount and diff < maxB:
            diff += 1
        if diff in bCount:
            bCount[diff] -= 1
            if bCount[diff] == 0: del (bCount[diff])
        else:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
