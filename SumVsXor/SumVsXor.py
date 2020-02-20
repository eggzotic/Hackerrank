#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    if n == 0: return 1
    # convert n to binary string
    binN = bin(n)[2:]
    # count all the bin strings with 0 in those positions
    bits = len(list(filter(lambda x: x != '1', binN)))
    return 1<<bits

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
