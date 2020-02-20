#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    n = len(A)
    # find each number, from 1, perform rotations to get it into position
    #  exclude n, n - 1 - conside them separately later
    aHash = {}
    bHash = {}
    for i in range(n):
        aHash[i] = A[i]
        bHash[A[i]] = i
    for i in range(n - 2):
        index = bHash[i + 1]
        while (index != i):
            if index - i == 1:
                bHash[aHash[index-1]] += 2
                bHash[aHash[index]] -= 1
                bHash[aHash[index + 1]] -= 1
                #
                temp = aHash[index-1]
                aHash[index-1] = aHash[index]
                aHash[index] = aHash[index + 1]
                aHash[index + 1] = temp
            else:
                # this is the "index - i >= 2" case
                bHash[aHash[index - 2]] += 2
                bHash[aHash[index-1]] -= 1
                bHash[aHash[index]] -= 1
                #
                temp = aHash[index - 2]
                aHash[index - 2] = aHash[index-1]
                aHash[index-1] = aHash[index]
                aHash[index] = temp
            index = bHash[i+1]
    # so n, n - 1: are either in order by now, or... cannot be
    return 'YES' if aHash[n-2] == n - 1 else 'NO'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
