#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    if len(s) <= 1:
        print('NO')
        return
    sWidth = math.floor(len(f'{s}') / 2)
    for width in range(1, sWidth + 1):
        last = s[:width]
        # leading zero on 2+ digit numbers are a fail
        if last[0] == '0' and width > 1:
            print('NO')
            return
        last = int(last)
        first = last
        cursor = width
        consecutive = True
        while consecutive:
            nextInt = last + 1
            nextWidth = len(f'{nextInt}')
            next = s[cursor: cursor + nextWidth]
            if (next[0] == '0' and width > 1) or int(next) != nextInt:
                consecutive = False
                break
            last = nextInt
            cursor += nextWidth
            if cursor >= len(s): break
        if consecutive:
            print(f'YES {first}')
            return
    print('NO')

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
