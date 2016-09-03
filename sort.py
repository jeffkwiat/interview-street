#!/bin/python

# question 
# input: a list of sorted arrays
# eg: 
#   [3, 6, 8, 8, 10]
#   [2, 10, 15]
#   [16, 30]
# output: the median number 
# eg: 8

import sys
import statistics

def get_median_value(list_numbers):
    ''' return the median value of the given list. '''
    return statistics.median(list_numbers)
    
if __name__ == '__main__':
    a = [3, 6, 8, 8, 10]
    b = [2, 10, 15]
    c = [16, 30]
    list_to_test = []
    list_to_test.extend(a)
    list_to_test.extend(b)
    list_to_test.extend(c)
    
    print(get_median_value(list_to_test))