#!/usr/bin/python3.4

class Matiere:

	def __init__(self, lst, index):
		self.note = list()
		for row in lst:
			try:
				self.note.append(float(row[index]))
			except:
				pass

	def get(self):
		return (self.note)
