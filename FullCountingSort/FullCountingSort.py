#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import repeat

# Complete the countSort function below.
def countSort(arr):
    indexArr = list(repeat(0, 100))
    sArr = []
    for _ in range(100):
        sArr.append([])
    ind = 0
    half = math.floor(len(arr) / 2)
    for item in arr:
        i = int(item[0])
        indexArr[i] += 1
        if ind < half:
            s = '-'
        else:
            s = item[1]
        sArr[i].append(s)
        ind += 1
    output = ''
    for item in filter(lambda x: len(x) > 0, sArr):
        output += ' ' + ' '.join(item)
    print(output[1:])

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
