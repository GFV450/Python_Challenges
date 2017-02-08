#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)


def diagonal_difference(a, n):
    diagOne = -1
    diagTwo = n
    sumOne = 0
    sumTwo = 0

    for x in a:
        diagOne += 1
        diagTwo -= 1

        sumOne += x[diagOne]
        sumTwo += x[diagTwo]

    return abs(sumOne - sumTwo)


answer = diagonal_difference(a, n)
print(answer)
