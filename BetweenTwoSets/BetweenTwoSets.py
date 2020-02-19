#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    gcf = 0
    for i in b:
        gcf = gcd(gcf, i)
    # print(f'gcd = {gcf}')
    #
    lc = 1
    for i in a:
        lc = lcm(lc, i)
    # print(f'lcm = {lc}')
    #
    tweens = []
    for i in range(lc, gcf +1, lc):
        if i % lc == 0 and gcf % i == 0:
            tweens.append(i)
    # print(tweens)
    return len(tweens)


def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return math.floor((a*b) / gcd(a, b))


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
