#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort()
    maxDiff = 4
    containers = 1
    minItem = w[0]
    for item in w[1:]:
        if item - minItem <= maxDiff: continue
        containers += 1
        minItem = item
    return containers

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
