#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    bigL = len(s)
    bigLRoot = math.sqrt(bigL)
    lower = math.floor(bigLRoot)
    upper = math.ceil(bigLRoot)
    r = lower
    c = upper
    if r * c < bigL: r = upper
    textBlock = []
    j = 0
    # produce the rows
    for _ in range(r):
        textBlock.append(s[j * c: min((j + 1) * c, bigL)])
        j += 1
    # extract the cols
    textCols = []
    for j in range(c):
        textCols.append(''.join(list(map(lambda row: row[j] if j < len(row) else '' , textBlock))))
    return ' '.join(textCols)

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
