#!/bin/python3

import sys

sentence = input().strip()
count = 0
if sentence:
    for letter in sentence:
        if letter.isupper():
            count += 1

    print(count + 1)
else:
    print(count)