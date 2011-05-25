# Find the number of ways a block of length 50 can be filled
# by black or red blocks

numWays = {}

def howManyWays (n) :
	try :
		return numWays[n]
	except :
		if n <= 0 :
			return 0
		if n == 1 or n == 2:
			return 1
		ret = 0
		ret += howManyWays(n-1)
		for i in range(3,n+1) :
			if i == n or i == n-1 :
				ret += 1
			else :
				ret += howManyWays(n-i-1)
		numWays[n] = ret
		return ret

print howManyWays(7)
print howManyWays(50)
		