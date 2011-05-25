# Find the smallest number of the longest amicable chain with
# no number over 1000000

# This is a GROSS solution
# Ran a brute force, didn't find any after one
# loop, checked each member of the chain manually

from useful import propDivisors
chains = {}

def chainLen(n,lis=[]) :
	if n in chains :
		return chains[n]
	if n > 1000000 :
		for i in lis :
			chains[i] = 0
		return 0
	if n in lis :
		for i in lis[:lis.index(n)] :
			chains[i] = 0
		for i in lis[lis.index(n):] :
			chains[i] = len(lis[lis.index(n):])
		# Found a loop!
		return len(lis[lis.index(n):])
	lis.append(n)
	dSum = sum(propDivisors(n))	
	return chainLen(dSum,lis)

k = 5916
for i in range(50) :
	print k
	k = sum(propDivisors(k))

"""m = 0
n = 0
for i in range(1000000) :
	if not i % 50000 :
		print i
	c = chainLen(i,[]) 
	if c > m :
		k = i
		k = sum(propDivisors(k))
		while k != i :
			print str(k) + " ",
			k = sum(propDivisors(k))
		print ""
		print i, c
		m = c
		n = i
print n"""