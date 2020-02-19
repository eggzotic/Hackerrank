#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    roundedGrades = []
    for grade in grades:
        if grade < 38 or grade % 5 == 0:
            roundedGrades.append(grade)
            continue
        nextMutipleOfFive = math.ceil(grade / 5) * 5
        if nextMutipleOfFive - grade < 3:
            roundedGrades.append(nextMutipleOfFive)
        else:
            roundedGrades.append(grade)
    return roundedGrades


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
