#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    i = k % n
    while i != 0:
        if c[i] == 1:
            e -= 3
        else:
            e -= 1
        i = (i + k) % n
    # so we're back to the 1st cloud - deduct according to it's value
    if c[0] == 1:
        e -= 3
    else:
        e -= 1
    return e


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
