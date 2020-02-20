#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    chars = set(s)
    if len(chars) < 2: return 0
    charList = list(chars)
    maxAlternatingLength = 0
    for a in charList:
        for b in charList:
            if a == b: continue
            newS = ''
            for c in s:
                if c == a or c == b: newS += c
            if isAlternating(newS):
                maxAlternatingLength = max(maxAlternatingLength, len(newS))
    return maxAlternatingLength

def isAlternating(s):
    # return True: if s is an alternating string of 2-chars only
    # return False otherwise
    chars = set(s)
    if len(chars) != 2: return False
    last = ''
    for c in s:
        if c == last: return False
        last = c
    return True

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
