# Find the number of sets so that each digi from 1-9 is used
# and all elements are prime.

from useful import powerset, isPrime, digitsToNum, allArrangements, memoize

def memoize(func) :
	def memoized_func(lis) :
		lis2 = frozenset(lis)
		d = {}
		if lis2 in d :
			return d[lis2]
		else :
			ret = func(lis)
			d[lis2] = ret
			return ret
	return memoized_func
	
def number(theDigs) :
	#global depth
	if len(theDigs) == 0 :
		#print depth
		return 1
	s = 0
	for digs2 in powerset(theDigs) :
		if digs2:
			count = 0
			for digs in allArrangements(digs2) :
				num = digitsToNum(digs)
				if isPrime(num) :
					count += 1
			if count > 0 :
				#for f in range(depth) :
				#	print " ",
				#print digs, num
				#depth.append(num)
				next = [x for x in theDigs if x not in digs]
				#print num, next
				s += count * number(next)
				#depth = depth[:-1]
	return s

number = memoize(number)

print number([1,2,3,4,5,6,7,8,9])