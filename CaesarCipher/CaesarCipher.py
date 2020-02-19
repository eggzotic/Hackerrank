#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    #
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    alpaLen = len(lowers)
    enc = {}
    for i in range(alpaLen):
        enc[lowers[i]] = lowers[(i + k) % alpaLen]
        enc[lowers[i].upper()] = enc[lowers[i]].upper()
    #
    newS = ''
    for c in s:
        if c in enc:
            newS += enc[c]
        else:
            newS += c
    return newS

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
