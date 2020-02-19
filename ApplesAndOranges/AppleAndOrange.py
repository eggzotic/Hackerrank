#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesOnHouse = 0
    orangesOnHouse = 0
    for apple in apples:
        location = apple +a
        if location >= s and location <= t:
            applesOnHouse += 1
    for orange in oranges:
        location = orange + b
        if location >= s and location <= t:
            orangesOnHouse += 1
    print(applesOnHouse)
    print(orangesOnHouse)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
