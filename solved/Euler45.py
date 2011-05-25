# After 40755, find the next triangle number that is pentagonal and hexagonal

from useful import doubleFactorize, primeFactorize, primeList, SortedList
import time

count = 120

tris = {}
pents = {}
hexes = {}

for i in range(300000) :
	tris[i*(i+1)/2] = True
	pents[i*(3*i-1)/2] = True

print (300000*(300001)/2)

while (True) :
	num = count*(2*count-1)
	if (tris.setdefault(num,False) and pents.setdefault(num,False)) :
		print num
	count += 1
	if num > (300000*(300001)/2) :
		break