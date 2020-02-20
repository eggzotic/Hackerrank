#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
shifts = 0
def runningTime(arr):
    insertionSort2(len(arr), arr)
    return shifts

def insertionSort2(n, arr):
    if n == 1:
        print(arr[0])
        return
    for i in range(1, len(arr)):
        arr = insertionSort1(i + 1, arr)
        # print(' '.join(map(str, arr)))

def insertionSort1(n, arr):
    global shifts
    x = arr[n - 1]
    found = False
    for i in range(n - 2, -1, -1):
        if arr[i] <= x:
            arr[i + 1] = x
            found = True
            break
        else:
            arr[i + 1] = arr[i]
            shifts += 1
    if not found: arr[0] = x
    return arr

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
