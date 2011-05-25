from useful import PrimeList

top = 50000000

primes = PrimeList(int(top**0.5 + 10))

cands = set([])

i = 0
psq = primes[i]
sq = psq*psq
while sq < top :
	j = 0
	pcub = primes[j]
	cub = pcub*pcub*pcub
	while sq + cub < top :
		k = 0
		pquar = primes[k]
		quar = pquar**4
		while sq + cub + quar < top :
			cands.add(sq+cub+quar)
			k += 1
			pquar = primes[k]
			quar = pquar**4
		j += 1
		pcub = primes[j]
		cub = pcub*pcub*pcub
	i += 1
	psq = primes[i]
	sq = psq*psq

print len(cands)