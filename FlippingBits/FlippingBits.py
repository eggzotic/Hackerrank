#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    # convert to binary-string, strip the leading '0b' and then pad to 32-bits
    bitString = bin(n)[2:].rjust(32, '0')
    # flip the bits
    flipped = bitString.replace('0', '2').replace('1', '0').replace('2', '1')
    # convert back to an int
    return int(flipped,2)

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
