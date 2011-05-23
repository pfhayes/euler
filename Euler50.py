# Find the prime below 1 000 000 that can be written as the longest sum of consecutive primes

from useful import primeList, SortedList

primes = primeList(1000000)
primes = SortedList(primes)

for i in range(547,0,-1) :
	for j in range(len(primes)-i) :
		#print "\t", j
		s = sum(primes[j:j+i])
		if s > 1000000 :
			break
		if s in primes :
			print s, primes[j:j+i]
			exit()