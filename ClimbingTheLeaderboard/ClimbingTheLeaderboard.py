#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    # a dup-free version of scores
    scoreSet = set(scores)
    # an ascending-ordered version of that
    sortedScores = sorted(scoreSet)
    places = []
    for a in alice:
        index = len(scoreSet) - bisect_right(sortedScores, a) + 1
        places.append(index)
        if a not in scoreSet:
            sortedScores.insert(len(scoreSet) - index + 1,a)
            scoreSet.add(a)
    return places

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
