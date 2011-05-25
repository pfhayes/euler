# Find the first odd composite number that cannot be written as the sum of a prime and two times a square.

from useful import primeList
from math import sqrt

pList = primeList(100000)

c = 7
while (True) :
	c += 2
	if c > 100000 :
		break
	if c in pList :
		continue
	else :
		for p in pList :
			if int(sqrt((c - p)/2))**2 == (c-p)/2 :
				break
		else :
			print c
			break