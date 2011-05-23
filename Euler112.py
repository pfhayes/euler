# Find the number for which the proportion of bouncy numbers below it is 99%

results = {}

def numIncreasing (digits, firstDigit) :
	if digits is 0 :
		return 0
	elif digits is 1 :
		return 1
	else :
		try :
			return results[(digits, firstDigit)]
		except :
			ret = sum([numIncreasing(digits-1, n) for n in range (firstDigit, 10)])
			results[(digits, firstDigit)] = ret
			return ret

def numBouncy (digits, firstDigit) :
	ret = 2*numIncreasing(digits+1,0)
	ret -= 10
	for i in range(2, digits) :
		ret += numIncreasing(digits+1,0)
		ret -= 9
	return ret + 1
	

print numBouncy(3,0)