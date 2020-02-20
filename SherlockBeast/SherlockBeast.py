#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    # n = 5x + 3y
    y = n // 3
    x5 = n - 3 * y
    while x5 % 5 != 0 and y > 0:
        y -= 1
        x5 = n - 3 * y
    if x5 % 5 == 0:
        print('5' * (3*y) + '3' * x5)
        return
    print('-1')

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
