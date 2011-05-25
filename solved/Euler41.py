# Find the largest prime that is n-digit pandigital

import sys
from useful import isPrime, digitsToNum

def perms (l) :
	if len(l) is 7 :
		if isPrime(digitsToNum(l)) :
			print "\t", l
			sys.exit(0)
		else :
			print l
	for i in range(7,0,-1) :
		if i in l :
			continue
		perms(l+[i])

perms([])