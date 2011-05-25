# Find the first pair of pentagonal numbers such that their sum and difference is a pentagonal number.

import sys
from useful import doubleFactorize
from math import sqrt

isPent = {1:True}
count = 2
numCandidates = 0

while (True) :
	newPent = (3*count*count-count)/2
	isPent[newPent] = True
	for i in range(1,count) :
		num1 = (3*i*i-i)/2
		if isPent.setdefault(newPent-num1, False) :
			sum = num1 + newPent
			for factors in doubleFactorize(2*sum) :
				if factors[0] == (factors[1]+1)/3 :
					print num1, newPent, newPent-num1
					numCandidates += 1
					break
	count += 1