#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    # just in case(!)
    s = s.lower()
    n = len(s)
    halfWidth = math.floor(n / 2)
    changeCount = 0
    for i in range(halfWidth):
        # compare symmetric values from each end
        #  the distance between them is the number of changes to make these 2 symmetric
        left = s[i]
        right = s[n - 1 - i]
        changeCount += abs(ord(left) - ord(right))
    return changeCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
