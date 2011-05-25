# Find the first four consecutive numbers to have 4 distinct prime factors.

from useful import primeList

count = 1000
numThatMatch = 0
pList = primeList(20000)

def primeFactorize (n) :
	primes = pList
	ret = []
	for p in primes :
		while n % p == 0 :
			ret.append(p)
			n /= p
		if n == 1 :
			return ret
	return ret

while True :
	count += 1
	factors = set(primeFactorize(count))
	print count, factors
	if len(factors) >= 4 :
		numThatMatch += 1
	else :
		numThatMatch = 0
	if numThatMatch == 4 :
		print count
		break