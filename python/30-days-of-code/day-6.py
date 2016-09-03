#!/bin/python3

import sys

n = int(input().strip())
words = []
for i in range(0, n):
    words.append(input().strip())
    
for word in words:
    even = ''
    odd = ''
    for letter_index in range(0, len(word)):
        if letter_index % 2 == 0:
            even += word[letter_index]
        else:
            odd += word[letter_index]
            
    print('%s %s' % (even, odd))