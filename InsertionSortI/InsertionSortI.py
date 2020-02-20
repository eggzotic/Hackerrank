#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    x = arr[n - 1]
    found = False
    for i in range(n - 2, -1, -1):
        if arr[i] < x:
            arr[i + 1] = x
            found = True
            break
        else:
            arr[i + 1] = arr[i]
        print(' '.join(map(str, arr)))
    if not found: arr[0] = x
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
