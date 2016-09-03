#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

negatives = 0
positives = 0
zeroes = 0

for i in range(0, n):
    if arr[i] > 0:
        positives += 1
    elif arr[i] < 0:
        negatives += 1
    else:
        zeroes += 1

print('%s\n%s\n%s' % (positives / n, negatives / n, zeroes / n))