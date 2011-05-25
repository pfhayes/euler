# Find the number of ways to fill a rectangle with blocks of length 1 and 2, 3, or 4

numWays = {}

def howManyWays (m, n) :
	try :
		return numWays[(m,n)]
	except :
		if n <= 0 :
			return 0
		if n == m:
			return 2
		if n >= 1 and n < m :
			return 1
		ret = 0
		ret += howManyWays(m,n-1)
		ret += howManyWays(m,n-m)
		numWays[(m,n)] = ret
		return ret

print howManyWays(2,50) + howManyWays(3,50) + howManyWays(4,50) - 3
