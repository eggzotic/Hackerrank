#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the bigSorting function below.
def bigSorting(unsorted):
    # this should be the correct solution
    #  but for a couple test cases it's still too slow
    # return sorted(unsorted, key=int)

    # So this is the fastest (by many miles!) although it's a bit weird to me
    #  how this works - some implicit magic where the outside sorted is
    #  behaving differently on the output from the inside sorted...?
    return sorted(sorted(unsorted), key=len)

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
