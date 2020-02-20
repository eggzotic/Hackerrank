#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    kNums = []
    for i in range(p, q + 1):
        d = len(f'{i}')
        iStr = f'{i * i}'
        lenIstr = len(iStr)
        r = iStr[lenIstr - d :]
        l = iStr[: lenIstr - d]
        if l == '': l = 0
        r = int(r)
        l = int(l)
        if r + l == i: kNums.append(f'{i}')
    if len(kNums) == 0:
        print('INVALID RANGE')
    else:
        print(' '.join(kNums))

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
