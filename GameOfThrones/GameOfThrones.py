#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    # count the occurrences of each char
    charCount = {}
    for c in s:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1
    # make sure all counts are even, except for, at most, 1
    odds = 0
    for value in charCount.values():
        if value % 2 == 1:
            odds += 1
            if odds > 1: return 'NO'
    return 'YES'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
