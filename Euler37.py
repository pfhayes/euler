# Find the only eleven primes that are truncatable from left to right and from right to left

from useful import digits, primeList, digitsToNum

isPrime = {}
primes = primeList(1000000)

sum = 0
for p in primes :
	isPrime[p] = True
	dList = digits(p)
	satisfies = True
	for i in range(1,len(dList)) :
		if not isPrime.setdefault(digitsToNum(dList[i:]),False) :
			satisfies = False
			break
	for i in range(1,len(dList)) :
		if not isPrime.setdefault(digitsToNum(dList[:i]),False) :
			satisfies = False
			break
	if satisfies :
		print p
		sum += p

print sum
		