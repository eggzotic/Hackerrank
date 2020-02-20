#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
