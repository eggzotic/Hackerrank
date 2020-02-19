#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    combos = itertools.combinations(ar, 2)
    tot = 0
    for c in combos:
        if (c[0] + c[1]) % k == 0:
            tot += 1
    return tot

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
