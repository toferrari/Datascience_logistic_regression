#!/usr/bin/python3.4

from describe import fill_note_house, fill_mat
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import sys
from read_csv import Read_csv
from matiere import Matiere

def check_empty(data):
	check = False
	while (check == False):
		check = True
		for i, row in enumerate(data):
			for j in range(6, len(row)):
				if (row[j] == ""):
					del data[i]
					check = False
	return data

def scatter_plt(note_house, name_house, name_mat):
	couleur = ['blue', 'red', 'green', 'yellow']
	x = name_mat.index('Arithmancy')
	y = name_mat.index('Care of Magical Creatures')
	# fig = plt.figure(1, figsize=(20, 10))
	plt.ylabel(name_mat[y])
	plt.xlabel(name_mat[x])
	for i in range(4):
		plt.scatter(note_house[i][y], note_house[i][x],s=1,\
		c=couleur[i], alpha=0.7)
	plt.savefig('Scatter_plot.png')

def main(train):
	data = Read_csv(train).get()
	data = check_empty(data)
	name_house = ["Hufflepuff", "Slytherin", "Ravenclaw", "Gryffindor"]
	note_house, name_mat = list(), list()
	name_mat = fill_mat(data)
	note_house = fill_note_house(data)
	scatter_plt(note_house, name_house, name_mat)

if __name__ == '__main__':
	main(sys.argv[1])
