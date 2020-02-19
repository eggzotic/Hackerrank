#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    # Write your code here.
    #
    hours = int(s[slice(2)])
    mins = s[slice(3, 5)]
    secs = s[slice(6, 8)]
    ampm = s[slice(8, 10)]
    if ampm == 'PM' and hours < 12: hours += 12
    if ampm == 'AM' and hours == 12: hours = 0
    return('%02d:%02s:%02s' %(hours,mins,secs))


if __name__ == '__main__':
    try:
        f = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        f = sys.stdout
    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
