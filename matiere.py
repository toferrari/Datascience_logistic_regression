#!/usr/bin/python3.4

class Matiere:

	def __init__(self, lst, index, house):
		self.note = list()
		for row in lst:
			try:
				if (house == "" or row[1] == house):
					self.note.append(float(row[index]))
			except:
				pass

	def get(self):
		return (self.note)
