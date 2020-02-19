#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    words = 1
    for c in s:
        if c.isupper(): words += 1
    return words

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
