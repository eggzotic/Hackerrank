#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    s1Counts = {}
    s2Counts = {}
    reductions = 0
    for c in set1:
        s1Counts[c] = s1.count(c)
    for c in set2:
        s2Counts[c] = s2.count(c)
    for c in set1 & set2:
        reductions += abs(s1Counts[c] - s2Counts[c])
    for c in set1 ^ set2:
        if c in set1:
            reductions += s1Counts[c]
        else:
            reductions += s2Counts[c]
    return reductions

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
