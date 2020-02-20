#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    unitAsWord = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }
    tensAsWord = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
    }
    #
    minStr = ''
    if m == 0:
        return f"{unitAsWord[h]} o' clock"
    elif m == 15:
        minStr = 'quarter past'
    elif m == 30:
        minStr = 'half past'
    elif m == 45:
        minStr = 'quarter to'
        h = (h + 1) % 12
        if h == 0: h = 12
    elif m < 20:
        minStr = f'{unitAsWord[m]} minute'
        if m > 1: minStr += 's'
        minStr += ' past'
    else:
        if m > 30:
            mins = 60 - m
            h = (h + 1) % 12
            if h == 0: h = 12
        else:
            mins = m
        if mins < 20:
            minStr = f'{unitAsWord[mins]} minute'
            minStr += 's' if mins > 1 else ''
        else:
            tenStr = tensAsWord[mins // 10]
            ones = mins % 10
            oneStr = f' {unitAsWord[ones]}' if ones != 0 else ''
            minStr = f'{tenStr}{oneStr} minutes'
        minStr += ' past' if m < 30 else ' to'
    return f'{minStr} {unitAsWord[h]}'

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
