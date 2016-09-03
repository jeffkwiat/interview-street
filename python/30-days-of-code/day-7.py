#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(' '.join([str(arr[x]) for x in range(n - 1, -1, -1)]))