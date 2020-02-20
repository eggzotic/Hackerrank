#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    # a hash for the weights of each char
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    weight = 0
    weightOf = {}
    for char in alphabet:
        weight += 1
        weightOf[char] = weight
    # a hash with:
    #  key: a continguous uniform substring of s
    #  value: the corresponding weight
    last = ''
    repeated = 1
    weightsFound = set()
    for c in s:
        if c == last:
            repeated += 1
        else:
            repeated = 1
            last = c
        weightsFound.add(repeated * weightOf[c])
    # check the numbers in queries for a matching weight
    return map(lambda q: 'Yes' if q in weightsFound else 'No', queries)

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
