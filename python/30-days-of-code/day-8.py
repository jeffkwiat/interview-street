#!/bin/python3

import sys


n = int(input().strip())
phone_book = {}
for i in range(0, n):
    name, phone_number = input().split(' ')
    phone_book[name] = phone_number

while True:
    try:
        query = input().strip()
        if query in phone_book:
            print('%s=%s' % (query, phone_book[query]))
        else:
            print('Not found')
    except:
        break