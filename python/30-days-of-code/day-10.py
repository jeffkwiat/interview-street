
#!/bin/python3

import sys

class Day10(object):
    def __init__(self, number):
        self.number = number
        
    def get_consecutive_ones(self):
        consecutive_ones = 0
        these_ones = 0
        for x in "{0:b}".format(self.number):
            if int(x) == 1:
                these_ones += 1
                if these_ones > consecutive_ones:
                    consecutive_ones = these_ones
                else:
                    these_ones = 0
        return consecutive_ones
        

        
if __name__ == '__main__':
    num = int(input())
    day10 = Day10(num)
    print(day10.get_consecutive_ones())