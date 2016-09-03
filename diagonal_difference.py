#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

class MatrixMath(object):
	def __init__(self, matrix):
		self.matrix = matrix

	def get_sum_first_diagonal(self):
		values = []
		column_index = 0
		for row_index in range(0, n):
			values.append(self.matrix[row_index][column_index])
			column_index += 1
		return sum(values)

	def get_sum_second_diagonal(self):
		values = []
		column_index = 0
		for row_index in range(n - 1, 0 - 1, -1):
			values.append(self.matrix[row_index][column_index])
			column_index += 1
		return sum(values)
	
	def get_diagonal_difference(self):
		return abs(self.get_sum_first_diagonal() - self.get_sum_second_diagonal())
	
if __name__ == '__main__':

	math = MatrixMath(a)
	print(math.get_diagonal_difference())
