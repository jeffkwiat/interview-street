#!/bin/python3

import sys

alice = input().strip().split(' ')
bob = input().strip().split(' ')

def print_sets(alice, bob):
	alice_score = 0
	bob_score = 0
	for index in range(0, len(alice)):
		if int(alice[index]) > int(bob[index]):
			alice_score += 1
		elif int(alice[index]) < int(bob[index]):
			bob_score += 1
	print("%s %s" % (alice_score, bob_score))
	
if __name__ == '__main__':
	print_sets(alice, bob)