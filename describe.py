#!/usr/bin/python3.4

from matiere import Matiere
from read_csv import Read_csv
import sys
import csv
from Libpy.maths import *

def fill_mat(data):
	name_mat = list()
	lengh = len(data[0])
	for i  in range(lengh):
		name_mat.append(data[0][i])
	for i in range(6):
		del name_mat[0]
	return (name_mat)

def fill_note(data, lengh):
	note = list()
	i = 6
	while (i < lengh):
		tmp = Matiere(data, i).get()
		note.append(tmp)
		i += 1
	return (note)

def count_all(note):
	count = list()
	for row in note:
		count.append(len(row))
	return (count)

def mean_all(note):
	mean = list()
	for row in note:
		mean.append(average(row))
	return(mean)

def std_all(note):
	std = list()
	for row in note:
		std.append(std_deviation(row))
	return(std)

def min_all(note):
	minn = list()
	for row in note:
		minn.append(ft_min(row))
	return(minn)

def quartile_all(note):
	div25, div50, div75 = list(), list(), list()
	for row in note:
		minn.append(quartile(row))
		minn.append(quartile(row))
		minn.append(quartile(row))
	return(minn)

def max_all(note):
	maxx = list()
	for row in note:
		maxx.append(ft_max(row))
	return(maxx)

def all_calcul(note):
	ret_data = list()
	ret_data.append(count_all(note))
	ret_data.append(mean_all(note))
	# ret_data.append(std_all(note))
	ret_data.append(min_all(note))
	ret_data.append(quartile_all(note))
	ret_data.append(max_all(note))
	return (ret_data)

def main(train):
	data = Read_csv(train).get()
	name_mat = fill_mat(data)
	note = fill_note(data, len(data[0]))
	ret_data = all_calcul(note)
	print ret_data

if __name__ == '__main__':
	main(sys.argv[1])
