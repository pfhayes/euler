# Finding primes with repeated digits.

from useful import isPrime, digitsToNum, digits

numlength = 10

def genAllLists(length, currNum, maxNum) :
	if length == 0 :
		return [[]]
	else :
		tabs = []
		for firstDig in range(currNum,maxNum+1) :
			for lis in genAllLists(length-1, firstDig, maxNum) :
				l = [firstDig]
				l.extend(lis)
				tabs.append(l)
		return tabs

totalSum = 0

for repeatedDigit in range(10) :
	primes = set([])
	for numRepeats in range(numlength-1,0,-1) :
		numUniques = numlength - numRepeats
		print repeatedDigit, numRepeats
		primeCount = 0
		primeSum = 0
		for i in range(10**numUniques) :
			uniqueDigs = digits(i,numUniques)
			for combo in genAllLists(numUniques,0,9) :
				digs = [repeatedDigit]*numRepeats
				for place in reversed(range(len(combo))) :
					digs[combo[place]:combo[place]] = [uniqueDigs[place]]
				if digs[0] == 0 :
					continue
				num = digitsToNum(digs)
				if num not in primes and isPrime(num) :
					#print num
					primes.add(num)
					primeCount += 1
					primeSum += num
		if primeCount > 0 :
			print "S(", numlength, ", ", repeatedDigit, ") =", primeSum
			totalSum += primeSum
			break

print totalSum
