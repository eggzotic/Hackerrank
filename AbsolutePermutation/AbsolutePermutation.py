#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    # special case
    if k == 0: return list(range(1, n + 1))
    #
    pos = []
    for i in range(1, n + 1):
        # smallest 1st (so lexicographic order is automatic)
        p = i - k
        q = i + k
        possibles = []
        if p >= 1: possibles.append(p)
        if q <= n: possibles.append(q)
        if len(possibles) == 0:  return [-1]
        pos.append(possibles)
    # now traverse the "tree" to find a valid permutation
    final = []
    # use a set to track usage - found that set-membership check is waaaaay faster than list-membership check
    used = set()
    for pList in pos:
        added = False
        for p in pList:
            if p in used: continue
            final.append(p)
            used.add(p)
            added = True
            break
        if not added: return [-1]
    return final

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
