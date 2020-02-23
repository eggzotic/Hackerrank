#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    lenN = len(n)
    total = 0
    digit = {}
    for i in range(10): digit[f'{i}'] = i
    tooBig = 1000000007  # pow(10, 9) + 7
    ones = 1
    # step thru 'n' in reverse order so as to ease the calculation of 'ones'
    #  which is really important for speed!
    for i in range(lenN - 1, -1, -1):
        total += (digit[n[i]] * ones * (i + 1)) % tooBig
        total %= tooBig
        ones = (ones * 10 + 1) % tooBig
    return total

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
