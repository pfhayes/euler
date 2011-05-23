# Find all circular primes below 1000000

from useful import primeList, digits

circulars = {}
isPrime = {}

def isCircular (n) :
	try :
		return circulars[n]
	except :
		if 0 in digits(n) :
			return False
		s = str(n)
		num = int(s[1:] + s[0])
		numList = [num]
		while (num != n) :
			s = str(num)
			num = int(s[1:] + s[0])
			numList.append(num)
		circular = True
		for i in numList :
			if not isPrime.setdefault(i,False) :
				circular = False
				break
		for i in numList :
			circulars[i] = circular
		return circular
		
pList = primeList(1000000)
for p in pList :
	isPrime[p] = True
count = 0
for p in pList :
	if isCircular(p) :
		count += 1
print count