#!/usr/bin/env python3

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
	for i in range(6, lengh):
		note.append(Matiere(data, i, "").note)
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
		tmp1, tmp2, tmp3 = quartile(row)
		div25.append(tmp1)
		div50.append(tmp2)
		div75.append(tmp3)
	ret = list()
	ret.append(div25)
	ret.append(div50)
	ret.append(div75)
	return(ret)

def max_all(note):
	maxx = list()
	for row in note:
		maxx.append(ft_max(row))
	return(maxx)

def all_calcul(note):
	ret_data = list()
	ret_data.append(count_all(note))
	ret_data.append(mean_all(note))
	ret_data.append(std_all(note))
	ret_data.append(min_all(note))
	ret_data.append(quartile_all(note))
	ret_data.append(max_all(note))
	return (ret_data)

def print_nb(nb):
	for i in range(len(nb)):
		print(repr(round(nb[i], 2)).rjust(20), end="")
	print()

def fill_note_house(data):
	note = list()
	Hufflepuff, Slytherin, Ravenclaw, Gryffindor = list(), list(), list(), list()
	for i in range(6, len(data[0])):
		Hufflepuff.append(Matiere(data, i, "Hufflepuff").note)
		Slytherin.append(Matiere(data, i, "Slytherin").note)
		Ravenclaw.append(Matiere(data, i, "Ravenclaw").note)
		Gryffindor.append(Matiere(data, i, "Gryffindor").note)
	note.append(Hufflepuff)
	note.append(Slytherin)
	note.append(Ravenclaw)
	note.append(Gryffindor)
	return (note)

def write_house(ret_house, name_mat, name_house):
	calcul = ["Count", "Mean", "Std", "Min", ["25%", "50%", "75%"], "Max"]
	for a in range(4):
		print("\n{}\n\t\t".format(name_house[a]), end="")
		for i in range(len(name_mat)):
			print(name_mat[i][:15].rjust(20), end="")
		print()
		for line in range(len(calcul)):
			if type(calcul[line]) != list:
				print ("{}\t\t".format(calcul[line]), end="")
				print_nb(ret_house[a][line])
			else:
				for line_l in range(len(calcul[line])):
					print ("{}\t\t".format(calcul[line][line_l]), end="")
					print_nb(ret_house[a][line][line_l])

def bonus(name_mat, data):
	note_house = list()
	note_house = fill_note_house(data)
	name_house = ["Hufflepuff", "Slytherin", "Ravenclaw", "Gryffindor"]
	ret_house = list()
	for i in range(4):
		ret_house.append(all_calcul(note_house[i]))
	write_house(ret_house, name_mat, name_house)

def write(name_mat, ret_data):
	calcul = ["Count", "Mean", "Std", "Min", ["25%", "50%", "75%"], "Max"]
	print("\t\t", end="")
	for i in range(len(name_mat)):
		print(name_mat[i][:15].rjust(20), end="")
	print()
	for line in range(len(calcul)):
		if type(calcul[line]) != list:
			print ("{}\t\t".format(calcul[line]), end="")
			print_nb(ret_data[line])
		else:
			for line_l in range(len(calcul[line])):
				print ("{}\t\t".format(calcul[line][line_l]), end="")
				print_nb(ret_data[line][line_l])

def main(train):
	data = Read_csv(train).get()
	name_mat = fill_mat(data)
	note = fill_note(data, len(data[0]))
	ret_data = all_calcul(note)
	write(name_mat, ret_data)
	bonus(name_mat, data)

if __name__ == '__main__':
	try:
		main(sys.argv[1])
	except:
		print("error")
