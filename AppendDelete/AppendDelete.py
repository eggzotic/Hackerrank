#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # find the length of the longest string
    lens = len(s)
    lent = len(t)
    n = max(lens, lent)
    divergenceIndex = min(lens,lent)
    for i in range(n):
        if i < lens and i < lent and s[i] == t[i]: continue
        divergenceIndex = i
        break
    stepsRequired = lens - divergenceIndex + lent - divergenceIndex
    # the 2nd condition below says that if the number of steps required is < k, by a multiple of 2
    #  then we can just perform dummy-append/delete pairs to take up the slack
    #
    # the 3rd condition below is what allows us to empty s and rebuild t,
    #  including any number of "delete from empty string"
    if stepsRequired == k or (k > stepsRequired and (k - stepsRequired) % 2 == 0) or lens + lent <= k:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
