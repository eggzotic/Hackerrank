#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    n = len(arr)
    forwardVal = 1
    reverseVal = 1
    forwards = [forwardVal]
    reverse = [reverseVal]
    # walk thru forwards - starting at 1, inc whenever there's a rise, reset to 1 otherwise
    # and simultaneously walk in reverse and inc whenever there's a rise, reset to 1 otherwise
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            forwardVal += 1
        else:
            forwardVal = 1
        forwards.append(forwardVal)
        if arr[n - 1 - i] > arr[n - i]:
            reverseVal += 1
        else:
            reverseVal = 1
        reverse.insert(0, reverseVal)
    result = []
    # now walk thru those and take the max value of each respective list
    for i, j in zip(forwards, reverse):
        result.append(max(i, j))
    return sum(result)

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
