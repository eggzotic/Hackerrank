#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0
    valleys = 0
    up = 'U'
    down = 'D'
    #
    for step in s:
        altitude += 1 if step == up else - 1
        if altitude == -1 and step == down: valleys += 1
    return valleys

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
