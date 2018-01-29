#!/usr/bin/python3.4

from describe import fill_note_house, fill_mat
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import sys
from read_csv import Read_csv
from matiere import Matiere
import seaborn as sns

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

def main(train):
	data = Read_csv(train).get()
	data = check_empty(data)
	name_house = ["Hufflepuff", "Slytherin", "Ravenclaw", "Gryffindor"]
	note_house, name_mat = list(), list()
	name_mat = fill_mat(data)
	note_house = fill_note_house(data)
	couleur = ['blue', 'red', 'green', 'yellow']
	fig = plt.figure(1, figsize=(25, 15))
	fig.subplots_adjust(bottom=0.05, left=0.05, top =0.99, right=0.99, \
	hspace=0.35, wspace=0.40)
	x, y, graph = 0, 0, 0
	for k in range(len(name_mat)):
		for l in range(len(name_mat)):
			if(x == 13):
				x = 0
				y += 1
			if (x == 5 and y == 5):
				plt.subplot(13,13,graph+3)
				axes = plt.gca()
				axes.set_frame_on(False)
				axes.xaxis.set_visible(False)
				axes.yaxis.set_visible(False)
				for i in range(4):
					plt.scatter(0,0, c=couleur[i], label=name_house[i], alpha=0.7)
					plt.legend()
			if (x <= y):
				plt.subplot(13,13,graph+1)
				if (x == 0):
					plt.ylabel(name_mat[y][:15], rotation=0)
				if (y == 12):
					plt.xlabel(name_mat[x][:15])
				if (x == y):
					for j in range(len(note_house)):
						plt.hist(note_house[j][x], alpha=0.7, color=couleur[j])
				else:
					for i in range(4):
						plt.scatter(note_house[i][y], note_house[i][x],s=1,\
						c=couleur[i], alpha=0.7)
			graph += 1
			x += 1
	plt.savefig('Pair_plot.png')
	# plt.show()

if __name__ == '__main__':
	main(sys.argv[1])
