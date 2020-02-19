#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    dop = 256
    day = 0
    finalMonth = 0
    for month in range(1,12+1):
        daysOfMonth = daysForMonth(year,month)
        if day + daysOfMonth < dop:
            day += daysOfMonth
        else:
            finalMonth = month
            break
    dom = dop - day
    return f'{str(dom).zfill(2)}.{str(finalMonth).zfill(2)}.{year}'


def daysForMonth(year, month):
    # Jan
    if month == 1: return 31
    # Feb
    if month == 2:
        if year < 1917:
            if year % 4 == 0:
                return 29
            return 28
        if year == 1918:
            return 15
        if year % 400 == 0: return 29
        if year % 100 == 0: return 28
        if year % 4 == 0: return 29
        return 28
    # Mar
    if month in [3, 5, 7, 8, 10, 12]: return 31
    return 30


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
