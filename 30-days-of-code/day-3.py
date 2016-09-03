#!/bin/python3

import sys


n = int(input().strip())


if n % 2 == 0:

    # If  is even and in the inclusive range of  to , print Not Weird
    if n >= 2 and n <= 5:
        print('Not Weird')
    # If  is even and in the inclusive range of  to , print Weird
    elif n >= 6 and n <= 20:
        print('Weird')
        
    # If  is even and greater than , print Not Weird
    elif n > 20:
        print('Not Weird')
else:
    print('Weird')
