#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    fwdDiffs = []
    last = s[0]
    for c in s[1:]:
        fwdDiffs.append(abs(ord(c) - ord(last)))
        last = c
    revDiffs = []
    last = s[len(s) - 1]
    for c in list(reversed(s))[1:]:
        revDiffs.append(abs(ord(c) - ord(last)))
        last = c
    for pair in zip(fwdDiffs, revDiffs):
        if pair[0] != pair[1]: return 'Not Funny'
    return 'Funny'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
