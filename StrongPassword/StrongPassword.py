#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # Rules:
    #  Its length >= 6
    #  It contains at least one digit.
    #  It contains at least one lowercase English character.
    #  It contains at least one uppercase English character.
    #  It contains at least one special character.
    specialCharacters = "!@#$%^&*()-+"
    #
    addLength = max(0, 6 - len(password))
    addDigit = 1
    addLower = 1
    addUpper = 1
    addSpecial = 1
    for c in password:
        if c.isdigit():
            addDigit = 0
        elif c.islower():
            addLower = 0
        elif c.isupper():
            addUpper = 0
        elif specialCharacters.count(c) > 0:
            addSpecial = 0
    return max(addDigit + addLower + addUpper + addSpecial, addLength)

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
