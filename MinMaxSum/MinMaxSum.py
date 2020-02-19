#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    # find the min & max values
    minVal = min(arr)
    maxVal = max(arr)
    # track the running totals in these
    total = 0
    # edge-case if all numbers the same
    for i in arr:
        total += i
    print(total - maxVal, total - minVal)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
