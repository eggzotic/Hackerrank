#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import repeat

# Complete the countingSort function below.
def countingSort(arr):
    indexArr = list(repeat(0, 100))
    for i in arr:
        indexArr[i] += 1
    return indexArr

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
