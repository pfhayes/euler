# Find the largest number that can be produced by taking an integer and 
# multiplying it by numbers 1..n such that the concatenated products form
# a 9-pandigital

from math import log10
from useful import digits

maxNum = 0

for i in range(10, 10000) :
	num = i
	count = 2
	while (num < 10**8) :
		newDigs = i*count
		num *= 10**int(log10(newDigs)+1)
		num += newDigs
		count += 1
	digs = digits(num)
	if (len(digs) == 9 and len(set(digs)) == 9 and 0 not in digs) :
		print i, count, num
		maxNum = max((maxNum,num))

print maxNum