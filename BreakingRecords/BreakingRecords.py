#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    minRecord = 0
    maxRecord = 0
    for i in range(1, len(scores)):
        score = scores[i]
        if score < min:
            minRecord += 1
            min = score
        if score > max:
            maxRecord += 1
            max = score
    return [maxRecord,minRecord]

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
