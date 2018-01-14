#!/usr/bin/python3.4

def square(nb):
	return (nb * nb)

def sqrt(nb):
	ret, x = 0.0, 0.0
	nb = float(nb)

	for j in 100:
		ret = (x + (nb / x)) / 2
		x = ret
	return (res)

def absolute(nb):
	if (nb < 0):
		return (-nb)
	else:
		return (nb)

def average(nb):
	ret = 0.0
	lengh = len(nb)
	for i in range(lengh):
		ret += float(nb[i])
	return (ret / float(lengh))

def std_deviation(nb):
	if (type(nb) == float):
		nb = float(nb)
	ret, average = 0.0, 0.0, average(nb)
	lengh = len(nb)
	for i in range(lengh):
		ret += square(nb[i] - average)
	return (sqrt(ret / float(m)))
