#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birdIdHash = {}
    maxSightings = 0
    maxSightingsId = 0
    for id in arr:
        if id in birdIdHash:
            birdIdHash[id] += 1
        else:
            birdIdHash[id] = 1
        if birdIdHash[id] > maxSightings:
            maxSightings = birdIdHash[id]
            maxSightingsId = id
        if birdIdHash[id] == maxSightings and id < maxSightingsId:
            maxSightingsId = id
    return maxSightingsId

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
