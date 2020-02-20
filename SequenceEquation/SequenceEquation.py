#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    results = []
    n = len(p) + 1
    for x in range(1, n):
        # find index of x (1-based)
        px = p.index(x) + 1
        # find the index of the value px (1-based)
        ppx = p.index(px) + 1
        results.append(ppx)
    return results

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
