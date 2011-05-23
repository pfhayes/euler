# Find a set of 5 primes for which any two primes concatenate to form another prime.

from useful import PrimeList, PrimeSet, digits, digitsToNum, isPrime
from math import log10

primes = PrimeList(10000)

search = 5

cands1 = set([frozenset([3])])
cands2 = set([frozenset([3])])

def makesPrimes(a,b) :
	if isPrime(a * 10**(int(log10(b))+1) + b) and isPrime(b * 10**(int(log10(a))+1) + a) :
		return True
	return False

count = 0

#Reconnaissance
for p in primes[2:] :
	#print p
	toAdd = set([])
	toRemove = set([])
	pool = sum(digits(p)) % 3
	if pool == 1 :
		targetSet = cands1
	else :
		targetSet = cands2
	for cand in targetSet :
		works = set([])
		for prime in cand :
			if makesPrimes(prime,p) :
				works.add(prime)
		if len(works) == len(cand) :
			toRemove.add(cand)
			toAdd.add(frozenset(cand | set([p])))
		else :
			toAdd.add(frozenset(works | set([p])))
		if len(cand) == search :
			print cand
			quit()
	if len(toAdd) == 0 :
		toAdd = set([frozenset([p])])
	targetSet -= toRemove
	targetSet |= toAdd