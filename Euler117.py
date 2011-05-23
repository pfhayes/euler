# Find how many ways there are to tile a row of fifty blocks
# using blocks of length 1,2,3 and 4

numWays = {}

def howManyWays (n) :
	try :
		return numWays[n]
	except :
		if n <= 0 :
			return 0
		if n == 1 :
			return 1
		if n == 2:
			return 2
		if n == 3:
			return 4
		if n == 4:
			return 8
		ret = 0
		ret += howManyWays(n-1)
		ret += howManyWays(n-2)
		ret += howManyWays(n-3)
		ret += howManyWays(n-4)
		numWays[n] = ret
		return ret
		
print howManyWays(50)