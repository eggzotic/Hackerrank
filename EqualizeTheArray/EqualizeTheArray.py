#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    # a set containing all unique elements of arr
    setArr = set(arr)
    # track the count of the most frequently occurring item
    topCount = 0
    for item in setArr:
        freq = arr.count(item)
        if freq > topCount:
            topCount = freq
    return len(arr) - topCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
