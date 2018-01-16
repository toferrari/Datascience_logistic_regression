#!/usr/bin/python3.4

import csv

class Read_csv:
	def __init__(self, name):
		self.name = name
		self.data = list()
		data_csv = csv.reader(open(self.name, "r"))
		for row in data_csv:
			self.data.append(row)

	def get(self):
		return (self.data)
