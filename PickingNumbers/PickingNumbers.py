#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    itemCount = {}
    for item in a:
        if item in itemCount:
            itemCount[item] += 1
        else:
            itemCount[item] = 1
    maxCount = 0
    sortedItems = sorted(list(itemCount.keys()))
    for item in sortedItems:
        thisMax = itemCount[item]
        for other in sortedItems:
            if item == other: continue
            if item - other == 1: thisMax += itemCount[other]
        maxCount = max(thisMax, maxCount)
    return maxCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
