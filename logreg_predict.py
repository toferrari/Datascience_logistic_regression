#!/usr/bin/python3.4

import sys
import numpy as np
from read_csv import Read_csv
import csv

def get_note(data):
	del data[0]
	for row in data:
		row[0] = 1
		del row[1:6]
	return (data)

def get_feat(note):
	index = [1, 2, 10, 11]
	for i, j in enumerate(reversed(index)):
		for row in note:
			del(row[j])
	return (note)

def check_empty(data):
	for i in range(len(data)):
		for k in range(len(data[i])):
			try:
				data[i][k] = float(data[i][k])
			except:
				data[i][k] = 0.0
	return (data)

def norme(note):
	n_norme, diviseur = list(), list()
	n_norme = note
	tmp_note = np.array(n_norme).T
	for row in tmp_note:
		if (np.abs(np.min(row)) > np.max(row)):
			diviseur.append(np.abs(np.min(row)))
		else:
			diviseur.append(np.max(row))
	for i, row in enumerate(n_norme):
		for j, nb in enumerate(row):
			n_norme[i][j] = n_norme[i][j] / diviseur[j]
	return (n_norme)

def sigmo(x):
	return (1/(1+np.exp(-x)))

def write_ret(index, house):
	if (index == 0):
		fthetha = open("house.csv", "w")
		fthetha.write("Index,Hogwarts House\n")
	else :
		fthetha = open("house.csv", "a")
	fthetha.write(str(index) + "," + str(house) + "\n")
	fthetha.close()

def test_theta(note, theta):
	tmp = np.array([0.0]*4)
	name = ["Hufflepuff", "Slytherin", "Ravenclaw", "Gryffindor"]
	i = 0
	for i in range(len(note)):
		for k in range(len(theta)):
			tmp[k] = sigmo(sum(note[i] * theta[k]))
		write_ret(i, name[np.argmax(tmp)])

def main(note_csv, theta_csv):
	data = csv.reader(open(theta_csv, "r"))
	theta = np.array([0.0]*4*10).reshape(4,10)
	for i, row in enumerate(data):
		for k in range(len(theta[i])):
			theta[i][k] = float(row[k])
	data = csv.reader(open(theta_csv, "r"))
	data = Read_csv(note_csv).get()
	note = get_note(data)
	note = get_feat(note)
	note = check_empty(note)
	note = norme(note)
	note = np.array(note)
	test_theta(note, theta)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
