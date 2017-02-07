#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diagOne = -1
diagTwo = len(a)
sumOne = 0
sumTwo = 0

for x in a:
    diagOne += 1
    diagTwo -= 1

    for y in x:
        if(x.index(y) == diagOne):
            sumOne += y

        if(x.index(y) == diagTwo):
            sumTwo += y

answer = abs(sumOne - sumTwo)
print(answer)
