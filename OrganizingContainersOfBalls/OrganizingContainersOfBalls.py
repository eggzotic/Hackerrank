#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    ballCountOfType = {}
    containerBallCount = {}
    # count the type of each by creating a dict
    for i in range(len(container)):
        row = container[i]
        containerBallCount[i] = sum(row)
        for j in range(len(row)):
            item = row[j]
            if j in ballCountOfType:
                ballCountOfType[j] += item
            else:
                ballCountOfType[j] = item
    # now ensure that there's a container whose ball-count matches the count of each type of ball present
    if set(ballCountOfType.values()) == set(containerBallCount.values()):
        return 'Possible'
    return 'Impossible'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
