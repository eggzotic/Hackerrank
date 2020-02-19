#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    n = len(s)
    hackerrank = 'hackerrank'
    hLen = len(hackerrank)
    hackFound = False
    hackLastFoundAt = -1
    for i in range(hLen):
        hackFound = False
        for j in range(max(i, hackLastFoundAt + 1), n):
            if s[j] == hackerrank[i]:
                hackFound = True
                hackLastFoundAt = j
                break
        if not hackFound: break
    # success if the last char has been found, otherwise not
    return 'YES' if hackFound else 'NO'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
