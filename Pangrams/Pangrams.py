#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s = s.lower()
    used = set()
    for c in s:
        if c.isalpha(): used.add(c)
        if len(used) == 26: return 'pangram'
    return 'not pangram'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
