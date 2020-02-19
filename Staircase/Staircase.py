#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    spaces = n - 1
    for _ in range(0, n):
        for j in range(0, n):
            if j < spaces:
                print(' ',end='')
            else:
                print("#",end='')
        spaces -= 1
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
