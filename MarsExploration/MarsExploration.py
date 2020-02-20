#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    changes = 0
    for i in range(0,len(s),3):
        if s[i] != 'S': changes += 1
        if s[i + 1] != 'O': changes += 1
        if s[i + 2] != 'S': changes += 1
    return changes

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout
        
    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
