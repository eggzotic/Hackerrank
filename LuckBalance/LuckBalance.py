#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    weightedContests = []
    freeLuck = 0
    for i in range(len(contests)):
        if contests[i][1] == 1:
            weightedContests.append(contests[i][0])
        else:
            freeLuck += contests[i][0]
    weightedContests.sort()
    weightedContests.reverse()
    luck = 0
    for i in range(len(weightedContests)):
        if i < k:
            luck += weightedContests[i]
        else:
            luck -= weightedContests[i]
    return luck + freeLuck

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
