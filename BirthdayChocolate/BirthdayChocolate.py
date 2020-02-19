#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.


def birthday(s, d, m):
    # generate the contiguous-combinations of m elements of s, whose values total d
    n = len(s)
    highestIndex = n - m + 1
    validComboCount = 0
    for i in range(highestIndex):
        if sum(s[i: i + m]) == d:
            validComboCount += 1
    return validComboCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
