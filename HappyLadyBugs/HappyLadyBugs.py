#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    # if any lonely char (occurs only once) exists then it's unhappy
    for i in set(b):
        if i != "_" and b.count(i) == 1: return "NO"

    # if there are no blanks then ensure the current layout is "happy"
    if b.count("_") == 0:
        for i in range(1, n - 1):
            if b[i - 1] != b[i] and b[i + 1] != b[i]: return "NO"

    # otherwise the assumption is that we can shuffle stuff around until they're happy!
    return "YES"

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
