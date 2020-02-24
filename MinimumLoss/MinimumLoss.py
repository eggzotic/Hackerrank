#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    # create a hash pointing to the original indices
    indexOf = {}
    for i in range(len(price)):
        indexOf[price[i]] = i
    # sort the prices so we can look at consecutive differences only
    price.sort()
    minLoss = pow(10,17)
    for i in range(1, len(price)):
        # check that the larger number (price[i]) originally came before the
        #  smaller (price[i-1]), i.e. check that we actually have a loss!
        if indexOf[price[i]] > indexOf[price[i - 1]]:
            continue
        loss = price[i] - price[i - 1]
        if loss < minLoss:
            minLoss = loss
    return minLoss

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
