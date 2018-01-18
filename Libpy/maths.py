#!/usr/bin/python3.4

def square(nb):
	return (nb * nb)

def sqrt(nb):
	ret, x = 0.0, 1.0
	nb = float(nb)

	for j in range(100):
		ret = (x + (nb / x)) / 2
		x = ret
	return (ret)

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
	ret, avge = 0.0, average(nb)
	lengh = len(nb)
	for i in range(lengh):
		ret += square(absolute(nb[i] - avge))
	return (sqrt(ret / float(lengh)))

def ft_min(nb):
	ret = nb[0]
	lengh = len(nb)
	for i in range(lengh):
		if (nb[i] < ret):
			ret = nb[i]
	return (ret)

def ft_max(nb):
	ret = nb[0]
	lengh = len(nb)
	for i in range(lengh):
		if (nb[i] > ret):
			ret = nb[i]
	return (ret)

def quartile(nb):
	nb.sort()
	lengh = len(nb)
	if (lengh % 4 == 0):
		div25 = lengh / 4
	else:
		div25 = lengh / 4 + 1
	if (lengh % 2 == 0):
		div50 = lengh / 2
	else:
		div50 = lengh / 2 + 1
	if (lengh % 0.75 == 0):
		div75 = lengh * 0.75
	else:
		div75 = lengh * 0.75 + 1
	return (nb[int(div25) - 1], nb[int(div50)], nb[int(div75)])
