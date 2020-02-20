#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.


def stones(n, a, b):
    if a == b:
        return [((n - 1) * a)]
    else:
        return [((i * max(a, b)) + ((n - i - 1) * min(a, b))) for i in range(n)]

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
