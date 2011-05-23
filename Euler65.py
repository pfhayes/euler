# Find the sum of the digits in the numerator of the 100th convergent of e

from useful import digits

def convergent(n) :
	if n == 1 :
		return (2,1)
	def recurseUpToN(step) :
		if step % 3 == 0 :
			val = 2*(step/3)
		else :
			val = 1
		if step == n :
			return (1,val)
		else :
			next = recurseUpToN(step+1)
			tup = (val * next[1] + next[0], next[1])
			return (tup[1],tup[0])
	ret = recurseUpToN(2)
	return (2 * ret[1] + ret[0],ret[1])

tup = convergent(100)
print tup

print sum(digits(tup[0]))