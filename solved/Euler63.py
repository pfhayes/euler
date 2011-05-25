# Find the number of n-digit positive integers that are also nth powers
# i.e. 16807 is 5 digits and a fifth power, 16807=7^5

from math import log10

num = 0
count = 1
while(True) :
	print num
	for i in range(1,10) :
		if int(log10(i**count)) == count - 1:
			num += 1
	count += 1
	