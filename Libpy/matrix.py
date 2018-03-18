#!/usr/bin/python3.4

def tranpose(matrix):
	res = list()
	for row in matrix :
		print(row)
	res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
	print("\n")
	for row in res:
		print(row)
	return (res)
