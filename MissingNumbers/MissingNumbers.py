#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    missing = set()
    for item in set(brr):
        if item not in arr or arr.count(item) < brr.count(item):
            missing.add(item)
    return sorted(list(missing))

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
