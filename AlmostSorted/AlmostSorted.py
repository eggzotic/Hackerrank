#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    sortedArr = sorted(arr)
    outOfPlace = {}
    # compare the before & after, 1-by-1
    for i in range(len(arr)):
        if arr[i] != sortedArr[i]: outOfPlace[i] = sortedArr[i]
    # if the list was already sorted - we're good
    if len(outOfPlace.keys()) == 0:
        print('yes')
        return
    # if there's exactly 2 out of order - we can swap
    if len(outOfPlace.keys()) == 2:
        indices = list(outOfPlace.keys())
        print('yes')
        print(f'swap {indices[0] + 1} {indices[1] + 1}')
        return
    # otherwise, len(outOfPlace) > 2, so the elements should be a contiguous block of indexes
    keys = outOfPlace.keys()
    minIndex = min(keys)
    maxIndex = max(keys)

    outOfPlaceIndexes = range(minIndex, maxIndex + 1)
    reversedIndexes = range(maxIndex, minIndex - 1, -1)
    for indexTuple in zip(reversedIndexes, outOfPlaceIndexes):
        rev = indexTuple[0]
        orig = indexTuple[1]
        if sortedArr[rev] != arr[orig]:
            print('no')
            return
    # success!
    print('yes')
    print(f'reverse {outOfPlaceIndexes[0] + 1} {outOfPlaceIndexes[len(outOfPlaceIndexes) - 1] + 1}')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
