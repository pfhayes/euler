#Find the number of reversible numbers below 10**9

from useful import digits

top = 9
n = 0
"""
for p in xrange(top) :
	print p
	for num in xrange(10**p,10**(p+1)) :
		if num % 10 == 0:
			continue
		carry = 0
		for i in xrange(p+1) :
			s = (num / 10**(p-i) % 10) + (num / 10**i % 10) + carry
			#print num, num / 10**(p-i) % 10, num / 10**i % 10, s
			if (s%2 == 0) :
				break
			carry = s/10
		else :
			n += 1

print n
""" #SLOW

