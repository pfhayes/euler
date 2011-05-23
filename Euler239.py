from useful import PrimeSet, choose, fact

numDiscs = 100
outOfOrder = 22

primes = PrimeSet(numDiscs)
numPrimes = len(primes)
numComps = numDiscs - numPrimes

def recurse(num,total) :
	if num == 0 :
		return (0,1)
	else :
		val = recurse(num-1,total)
		first = (num-1) * val[0]
		second = (val[1] - first)
		return (second, first*(total-num+1) + second*(total-num))

def ways(num,total) :
	return recurse(num,total)[1]

top = choose(numPrimes,outOfOrder) * ways(outOfOrder,numDiscs-numPrimes+outOfOrder) * fact(numComps)
bottom = fact(numDiscs)

print float(top)/bottom