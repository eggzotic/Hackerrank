#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    indices = isPalindrome(s)
    if indices[0] == -1:
        return (-1)
    #
    if len(indices) > 1:
        # try removing each and checking
        left = isPalindrome(s[: indices[0]] + s[indices[0] + 1 :])
        if left[0] == -1: return indices[0]
        right = isPalindrome(s[: indices[1]] + s[indices[1] + 1 :])
        if right[0] == -1: return indices[1]
    return (-1)

def isPalindrome(s):
    n = len(s)
    half = math.floor(n / 2)
    for i in range(half):
        if s[i] != s[n - i - 1]:
            return [i, n - i - 1]
    return [-1]

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
