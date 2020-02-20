#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    charCount = {}
    for c in s:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1
    values = set(charCount.values())
    n = len(values)
    if n == 1: return 'YES'
    if n >= 3: return 'NO'
    # so there's 2 values
    biggest = max(values)
    smallest = min(values)
    if list(charCount.values()).count(biggest) == 1 and biggest == smallest + 1: return 'YES'
    if smallest == 1 and list(charCount.values()).count(smallest) == 1: return 'YES'
    return 'NO'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
