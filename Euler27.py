# Find the quadratic formula n^2 + an + b that produces the most consecutive primes from n = 0...
# with |a|,|b| < 1000

from useful import primeList

primes = primeList(10000)
mostPrimes = 0
maxA = 0
maxB = 0

for a in range(-999,1000) :
	print a
	for b in range(-999,1000) :
		n = 0
		while (n*n + a*n + b in primes) :
			n += 1
		mostPrimes = max((mostPrimes, n))
		if n == mostPrimes :
			maxA = a
			maxB = b

print mostPrimes, maxA, maxB
		