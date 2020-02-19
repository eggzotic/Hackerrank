#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    n = len(A)
    #
    aRev = {}
    bRev = {}
    for i in range(n):
        if A[i] in aRev:
            aRev[A[i]].append(i)
        else:
            aRev[A[i]] = [i]
        #
        if B[i] in bRev:
            bRev[B[i]].append(i)
        else:
            bRev[B[i]] = [i]
    # print(f'aRev: {aRev}')
    # print(f'bRev: {bRev}')
    bps = 0
    for val in aRev.keys():
        if val not in bRev: continue
        while len(aRev[val]) > 0 and len(bRev[val]) > 0:
            aRev[val].pop()
            bRev[val].pop()
            bps += 1
    # print(f'aRev: {aRev}')
    # print(f'bRev: {bRev}')
    # and now to try to use our free 1-change
    used = False
    for thing1 in aRev.keys():
        if len(aRev[thing1]) > 0:
            for thing2 in bRev.keys():
                if len(bRev[thing2]) > 0:
                    used = True
                    break
            if used: break
    if used:
        bps += 1
    else:
        # we actually cannot make a change without losing a pair
        bps -= 1
    #
    return bps

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
