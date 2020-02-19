#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    changeCount = 0
    # eliminate "doubles" (i.e. 01010) with a single change in the common 0 digit
    while b.count('01010') > 0:
        index = b.index('01010')
        b = b[:index] + '01110' + b[index + 5 :]
        changeCount += 1
    # then eliminate the remaining singles
    while b.count('010') > 0:
        index = b.index('010')
        b = b[:index] + '011' + b[index + 3 :]
        changeCount += 1
    return changeCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
