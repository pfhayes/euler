# Find the number for which n / phi(n) is maximized, where phi(n) is the number
# of numbers below n that are relatively prime to n

# Since phi(n^m) = n^(m-1)*phi(n).
# then (n^m) / phi(n^m) is constant for all m >= 1

from useful import PrimeList, phi

primes = PrimeList(1000001)
cands = set(range(2,1000001))

print "Ready!"

for p in primes :
	temp = p
	while temp < 1000001 :
		cands.remove(temp)
		temp *= p

for c in range(2,1001):
	temp = c
	temp *= c
	while temp < 1000001 :
		cands.discard(temp)
		temp *= c

ma = 0
best = 0
for cand in reversed(list(cands)) :
	val = float(cand) / phi(cand)
	if val > ma :
		ma = val
		best = cand
		print best
		