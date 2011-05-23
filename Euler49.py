# Find the only other 3-term, 4-digit arithmetic sequence where all terms are prime and all terms
# contain the same digits
# One is 1487, 4817, 8147

from useful import digits, primeList

primes = primeList(10000)
nums = {}

for p in primes :
	digs = digits(p)
	digs.sort()
	dT = tuple(digs)
	val = nums.setdefault(dT, [0,[]]) 
	val[0] += 1
	val[1].append(p)
	nums[dT] = val

for k in nums.keys() :
	if nums[k][0] >= 3 :
		this = nums[k][1]
		this.sort()
		for i in range(len(this)) :
			for j in range(i+1,len(this)) :
				for k in range(j+1, len(this)) :
					if this[j] - this[i] == this[k] - this[j] :
						print this[i], this[j], this[k]
						

