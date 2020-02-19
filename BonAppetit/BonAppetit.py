#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.


def bonAppetit(bill, k, b):
    billTotal = sum(bill)
    annaShouldPay = math.floor((billTotal - bill[k]) / 2)
    diff = b - annaShouldPay
    if diff == 0:
        print('Bon Appetit')
    else:
        print(diff)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
