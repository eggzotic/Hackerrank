#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    sharedCount = 5
    likedCount = 0
    for day in range(n):
        newLikes = math.floor(sharedCount / 2)
        likedCount += newLikes
        sharedCount = newLikes * 3
    return likedCount

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
