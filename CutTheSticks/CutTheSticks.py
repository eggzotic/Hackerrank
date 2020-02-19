#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    piecesCount = []
    n = len(arr)
    while n > 0:
        piecesCount.append(n)
        # find the shortest piece
        shortest = min(arr)
        # and how many occurrences of it
        shortestCount = arr.count(shortest)
        # then remove those shortest pieces
        for i in range(shortestCount):
            arr.remove(shortest)
            # which reduces the arr length
            n -= 1
        # cut the remaining sticks by that shortest length
        for i in range(n):
            arr[i] -= shortest
    return piecesCount


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
