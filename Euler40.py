# Find the 1th,10th,100th,...,1000000th digits of the decimal 
# 0.1234567891011121314...

count = 1
num = 1
ret = []

from math import log10
from useful import digits

while (count <= 1000001) :
	for dig in digits(num) :
		if count in [1,10,100,1000,10000,100000,1000000] :
			ret.append(dig)
		count += 1
	num += 1

print ret