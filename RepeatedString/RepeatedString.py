#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    aCount = s.count('a')
    sLen = len(s)
    total = (n // sLen) * aCount
    extra = n % sLen
    for i in range(extra):
        if s[i] == 'a': total += 1
    return total

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
