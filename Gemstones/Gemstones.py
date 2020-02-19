#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    rockCount = len(arr)
    mineralOccurrences = {}
    for rock in arr:
        mineralFound = set()
        for mineral in rock:
            if mineral in mineralFound: continue
            mineralFound.add(mineral)
            if mineral in mineralOccurrences:
                mineralOccurrences[mineral] += 1
            else:
                mineralOccurrences[mineral] = 1
    gemstoneCount = 0
    for mineral in mineralOccurrences.keys():
        if mineralOccurrences[mineral] == rockCount: gemstoneCount += 1
    return gemstoneCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
