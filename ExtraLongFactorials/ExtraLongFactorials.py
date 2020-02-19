#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    result = n
    for i in range(1, n):
        result *= i
    print(result)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
