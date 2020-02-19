#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theGreatXor function below.
def theGreatXor(x):
    # calculate the positions of the 0 bits
    #  and then calculate the maximum number representable by those
    binX = list(reversed(bin(x)[2:]))
    total = 0
    for i in range(len(binX)):
        if binX[i] == '0': total += 1 << i
    return total

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
