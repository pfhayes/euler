# Find the value of n where phi(n) is a permutation of n
# and n/phi(n) is minimized for 1 < n < 10**7

from math import log10
from useful import PrimeList, digits

primes = PrimeList(int(10**3.5)+1)

def primeFactorize (n) :
	ret = []
	sq = n**0.5
	for p in primes :
		if p > sq :
			break
		while n % p == 0 :
			ret.append(p)
			n /= p
		if n == 1 :
			return ret
	return ret + [n]

def phi(n) :
	facts = primeFactorize(n)
	if len(facts) == 1:
		return n-1
	ret = n
	for fact in facts :
		ret /= fact
		ret*= fact-1
	return ret

minVal = 100
for num in xrange(10**7,1,-1) :
	ph = phi(num)
	if float(num)/ph < minVal and int(log10(ph)) == int(log10(num)) :
		digsp = digits(ph)
		digsn = digits(num)
		for dig in digsp :
			if dig in digsn :
				digsn.remove(dig)
			else :
				break
		else :
			print num
			minVal = float(num)/ph
			print minVal