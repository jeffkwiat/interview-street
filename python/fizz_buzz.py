#!/bin/python3

def fizz_buzz(min, max):
	for number in range(min, max):
		message = ''
		if number % 3 == 0:
			message += 'Fizz'
		if number % 5 == 0:
			message += 'Buzz'
		print(message or number)
		
if __name__ == '__main__':
	fizz_buzz(1, 11)