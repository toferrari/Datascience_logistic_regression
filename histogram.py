#!/usr/bin/env python3

from describe import fill_note_house, fill_mat
import matplotlib.pyplot as plt
import csv
import sys
from read_csv import Read_csv
from matiere import Matiere

def histo(note_house, name_mat, name_house):
	fig = plt.figure(1, figsize=(25, 15))
	for i in range(len(note_house[0])):
		plt.subplot(4,4,i+1)
		plt.title(name_mat[i])
		for j in range(len(note_house)):
			plt.hist(note_house[j][i], alpha=0.4, label=name_house[j])
			plt.legend(loc = 'upper left')
	plt.savefig('png/Histograme.png')

def main(train):
	data = Read_csv(train).get()
	name_house = ["Hufflepuff", "Slytherin", "Ravenclaw", "Gryffindor"]
	note_house, name_mat = list(), list()
	name_mat = fill_mat(data)
	note_house = fill_note_house(data)
	histo(note_house, name_mat, name_house)

if __name__ == '__main__':
	try:
		main(sys.argv[1])
	except:
		print("error")
