#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    halfn = math.floor(n / 2)
    # the left-side (or 1st-half) of the final palindrome, using the hash keys
    #  to represent the index into the final string
    upgraded = {}
    # note which positions *must* be changed to create a palindrome (or if it's even possible)
    changes = 0
    for i in range(halfn):
        left = i
        right = n - 1 - i
        if s[left] != s[right]:
            changes += 1
            if changes > k: return '-1'
            upgraded[left] = max(s[left],s[right])
    # Look at upgrading chars to 9
    nine = '9'
    haveToChange = changes
    i = 0
    changes = 0
    while changes + haveToChange < k and i < halfn:
        if i in upgraded:
            haveToChange -= 1
            if upgraded[i] == nine:
                # effectively 1 change - to match an initially non-symmetric 9
                changes += 1
            elif changes + haveToChange < k:
                # effectively 2 changes - to a pair of initially non-symmetric chars
                upgraded[i] = nine
                changes += 2
        elif changes + haveToChange < k - 1:
            if s[i] != nine:
                # effectively 2 changes (to original matched non-9)
                upgraded[i] = nine
                changes += 2
        i += 1
    # if n is odd, we should consider the middle char for "upgrade to 9" also
    if n % 2 == 1:
        if changes + haveToChange < k:
            upgraded[halfn] = nine
        else:
            upgraded[halfn] = s[halfn]
    # fill-out the remainder of the upgraded hash
    for i in range(halfn):
        if i not in upgraded: upgraded[i] = s[i]
    #
    # the upgraded string
    return ''.join([upgraded[i if i < halfn else n - 1 - i] for i in range(n)])

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
