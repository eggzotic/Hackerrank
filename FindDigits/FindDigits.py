#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    nAsString = f'{n}'
    digitFactors = 0
    for digit in nAsString:
        d = int(digit)
        if d == 0: continue
        if n % d == 0: digitFactors += 1
    return digitFactors

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
