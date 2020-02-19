#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    n = len(s)
    halfn = math.floor(n / 2)
    if n % 2 == 1: return - 1
    s1 = s[:halfn]
    s2 = s[halfn:]
    diffs = 0
    for c in set(s):
        diffs += abs(s1.count(c) - s2.count(c))
    return math.floor(diffs / 2)

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
