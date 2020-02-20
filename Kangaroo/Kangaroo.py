#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.


def kangaroo(x1, v1, x2, v2):
    if v2 >= v1:
        return 'NO'

    jumps = (x1 - x2) / (v2 - v1)
    if jumps - math.floor(jumps) == 0 and jumps >= 0:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
