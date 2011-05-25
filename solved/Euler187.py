from useful import PrimeList

m = 10**8
primes = PrimeList(m)
print "Done primes"

count = 0

for i in xrange(len(primes)) :
	for j in xrange(i,len(primes)) :
		if primes[i]*primes[j] >= m :
			break
		count += 1
print count