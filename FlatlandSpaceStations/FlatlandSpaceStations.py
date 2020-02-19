#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    m = len(c)
    spaceStationDistance = {}
    for city in c:
        spaceStationDistance[city] = 0
    #
    for city in range(n):
        if city in spaceStationDistance: continue
        left = bisect_right(c, city)
        if left == 0:
            # at the beginning
            spaceStationDistance[city] = c[0] - city
        elif left == m:
            # at the end
            spaceStationDistance[city] = city - c[m - 1]
        else:
            # in between to stations
            # print(f'city = {city}, left = {left}, c = {c}')
            d1 = city - c[left - 1]
            d2 = c[left] - city
            spaceStationDistance[city] = min(d1,d2)
    return max(set(spaceStationDistance.values()))

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
