#!/bin/python3

import sys


N = int(input().strip())
for i in range(1, 11):
    print('%s x %s = %s' % (N, i, N * i))