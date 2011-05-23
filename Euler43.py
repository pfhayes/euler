# Find the sum of all 0 to 9 pandigital primes where
# d2-4 is divisible by 2, d3-5 is divisible by 3, d4-6 is divisible by 5
# and so on through the primes

from useful import digits, primeList, digitsToNum

primes = primeList(18)
sum = [0]

def satisfies(threeDigs, primeIndex, allDigsSoFar) :
	if primeIndex == 0 :
		if threeDigs % 2 == 0 and len(set(allDigsSoFar)) == 9 :
			count = 0
			while (count < 10)  :
				if count not in allDigsSoFar :
					break
				count += 1
			val = digitsToNum([count] + allDigsSoFar)
			print val
			sum[0] += val
	lastTwoDigs = threeDigs/10
	for i in range(10) :
		if (i * 100 + lastTwoDigs) % primes[primeIndex-1] == 0 and i not in allDigsSoFar :
			satisfies(i*100+lastTwoDigs, primeIndex-1, [i] + allDigsSoFar)

for j in range(6,59) :
	digs = digits(j*17,3)
	if len(set(digs)) == 3:
		satisfies(j*17,6,digs)

print sum