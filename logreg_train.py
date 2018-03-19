#!/usr/bin/python3.4

from describe import fill_note_house, fill_mat
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import sys
from read_csv import Read_csv
from matiere import Matiere
from Libpy.matrix import *
from Libpy.maths import *

def check_empty(data, index):
	check = False
	while (check == False):
		check = True
		for i, row in enumerate(data):
			for j in range(6, len(row)):
				if (((j - 6) in index) == True and row[j] == ""):
					del data[i]
					check = False
	return data

def get_feat(note):
	index = [1, 2, 10, 11]
	for i, j in enumerate(reversed(index)):
		for row in note:
			del(row[j])
	return (note)

def get_note(data):
	del data[0]
	for row in data:
		row[0] = 1
		del row[1:6]
	return data

def get_house(data):
	house = list()
	for row in data:
		house.append(row[1])
	return house

def norme(note):
	n_norme, diviseur = list(), list()
	n_norme = note
	for row in note:
		if (absolute(ft_min(row)) > ft_max(row)):
			diviseur.append(absolute(ft_min(row)))
		else:
			diviseur.append(ft_max(row))
	for i, row in enumerate(n_norme):
		for j, nb in enumerate(row):
			n_norme[i][j] = n_norme[i][j] / diviseur[i]
	return (n_norme, diviseur)

def train_theta(n_norme, house):
	theta = 4*[10*[0.0]]
	i = 0
	# while (1 < 1000):
	# 	for

def main(train):
	index = [2, 3, 4, 5, 6, 7, 8, 11, 12]
	data = Read_csv(train).get()
	data = check_empty(data, index)
	note, house = list(), list()
	note = get_feat(get_note(data))
	house = get_house(data)
	note = [[float(y) for y in x] for x in note]
	note = tranpose(note)
	n_norme, diviseur = norme(note)
	train_theta(n_norme, house)
	# print (len(note))
	# print (len(house))
	# print(type(note[1]))
	# print (sum(note[1])/len(note[1]))

if __name__ == '__main__':
	main(sys.argv[1])
