#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.


def strangeCounter(t):
    # 1. divide-by 3, & round-up
    # 2. convert to binary, count how many bits (n) (note the " - 2" is because bin() prefixes the binary-format number with '0b')
    # 3. convert that to the all ones (2^n - 1), by left-shifting n-bits and subtracting 1
    # 4. then multiply by 3 -> this is the last "t" for the same cycle as original t
    # 5. add-one and this is the total t + value(t) for all t in this cycle
    # 6. so total - t -> value(t)
    cycleTotal = int((1 << (len(bin(math.ceil(t / 3))) - 2)) - 1) * 3 + 1
    return cycleTotal - t


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
