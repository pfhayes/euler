# Find the number of ways to fill a row of length n with blocks of size 1 and m
# When m = 50, find the first value of n where f(m,n) exceeds one million

numWays = {}

def howManyWays (m, n) :
	try :
		return numWays[(m,n)]
	except :
		if n <= 0 :
			return 0
		if n == 1 or n == 2:
			return 1
		ret = 0
		ret += howManyWays(m,n-1)
		for i in range(m,n+1) :
			if i == n or i == n-1 :
				ret += 1
			else :
				ret += howManyWays(m,n-i-1)
		numWays[(m,n)] = ret
		return ret

curr = 55
while (True) :
	if howManyWays(50,curr) > 1000000 :
		print curr
		break
	curr+= 1