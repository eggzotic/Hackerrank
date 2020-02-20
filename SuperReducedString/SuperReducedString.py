#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    while True:
        dupFound = False
        for i in range(1,len(s)):
            if s[i] != s[i - 1]: continue
            dupFound = True
            # slice out the consecutive dup
            s = s[: i - 1] + s[i + 1 :]
            break
        if not dupFound: break
    if s == '' : return 'Empty String'
    return s

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
