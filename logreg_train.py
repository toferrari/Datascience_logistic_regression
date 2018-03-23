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
import numpy as np
from math import *

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
	house = list()
	for row in data:
		house.append(row[1])
		row[0] = 1
		del row[1:6]
	return (data, house)

def get_house(data):
	house = list()
	for row in data:
		house.append(row[1])
	return house

def norme(note):
	n_norme, diviseur = list(), list()
	n_norme = note
	tmp_note = np.array(n_norme).T
	print(len(tmp_note))
	for row in tmp_note:
		if (absolute(ft_min(row)) > ft_max(row)):
			diviseur.append(absolute(ft_min(row)))
		else:
			diviseur.append(ft_max(row))
	for i, row in enumerate(n_norme):
		for j, nb in enumerate(row):
			n_norme[i][j] = n_norme[i][j] / diviseur[j]
	return (n_norme, diviseur)

def bool_house(house):
	name = ["Hufflepuff", "Slytherin", "Ravenclaw", "Gryffindor"]
	house_b = np.array([0.0]*4*len(house)).reshape(4,len(house))
	for i in range(len(house_b)):
		for y in range(len(house)):
			if (house[y] == name[i]):
				house_b[i][y] = 1.0
			else :
				house_b[i][y] = 0.0
	return(house_b)

def sigmo(x):
	return (1/(1+np.exp(-x)))

def up_theta(note, theta, y, house):
	ret = 0.0
	ret = sum((sigmo(note.dot(theta.T)) - house) * (note.T)[y]) / float(len(note))
	return (ret)

def cost(note, theta, house):
	ret = 0.0
	sig = sigmo(note.dot(theta.T))
	ret = -sum((house * np.log(sig)) + ((1.0 - house) * np.log(1.0 - sig))) / float(len(note))
	return (ret)

def train_theta(note, house, diviseur):
	tmp_theta = np.array([0.0]*4*10).reshape(4,10)
	theta = np.array([0.0]*4*10).reshape(4,10)
	note = np.array(note)
	house = bool_house(house)
	t = np.array([0]*4)
	m = float(len(note[0]))
	tmp_cost = np.array([0]*4)
	theta_cost = np.array([0.0]*4)
	print (note[0])
	while (sum(t) != 4):
		theta_cost = [cost(note, theta[i], house[i]) for i in range(len(theta_cost))]
		for i in range(len(theta)):
			for y in range(len(theta[i])):
				# print (theta_cost)
				if (round(theta_cost[i],3) < 0.07):
					t[i] = 1
				else:
					tmp_theta[i][y] -= up_theta(note, theta[i], y, house[i])
		theta = tmp_theta
		# print(theta_cost)

	# print(len(diviseur))
	# theta = theta * diviseur
	print (theta[0])
	note = note * diviseur
	b = sigmo(sum(note[0] * (theta[0].T)))
	print (len(note[0]))
	print (len(theta[0]))
	print (b)
	# for a in range(10):
	# 	print("\n")
	# 	for i in range(4):
	# 		sig = sigmo(note[a].dot(theta[i]))
	# 		print (sig)
	# test = cost(note, theta[0], house[0])
	# print (test)
	# tmp = list()
	# print (note[1])
	# for i in range(len(theta)):
	# 	print (theta[i])
	# 	tmp.append(sum(theta[i] * note[1]))
	# print (tmp)

def main(train):
	index = [2, 3, 4, 5, 6, 7, 8, 11, 12]
	data = Read_csv(train).get()
	data = check_empty(data, index)
	note, house = list(), list()
	note, house = get_note(data)
	note = get_feat(note)
	note = [[float(y) for y in x] for x in note]
	n_norme, diviseur = norme(note)
	array = np.array(n_norme)
	train_theta(n_norme, house, diviseur)

if __name__ == '__main__':
	main(sys.argv[1])
