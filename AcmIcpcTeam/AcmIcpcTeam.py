#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    decTopics = []
    for t in topic:
        decTopics.append(int(t, 2))
    decPairs = []
    for i in range(len(decTopics)):
        for j in range(i + 1, len(decTopics)):
            decPairs.append(decTopics[i] | decTopics[j])
    topicCounts = list(map(lambda x: bin(x).count('1'), decPairs))
    bestCount = max(topicCounts)
    freq = topicCounts.count(bestCount)
    return [bestCount,freq]

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
