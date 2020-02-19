#!/bin/python3

import os
import sys
import math

#
# Complete the pageCount function below.
#


def pageCount(n, p):
    #
    # Write your code here.
    #
    # from the start, p = 2 * pt, 2 * pt + 1
    # from the end:
    #   if n is even: p = n - 2 * pt, n - 2 * pt + 1
    #   if n is odd: p = n - 2 * pt - 1, n - 2 * pt
    if p == 1 or p == n:
        return 0
    if p % 2 == 1:
        evenPage = p - 1
    else:
        evenPage = p

    # calculations from the start are always like this
    fromStart = math.floor(evenPage / 2)
    # calculations from the end depends on whether n is odd or even
    if (n % 2 == 1):
        fromEnd = math.floor((n - evenPage - 1)/2)
    else:
        fromEnd = math.floor((n - evenPage) / 2)
    #
    return min(fromStart, fromEnd)


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
