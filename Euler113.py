# A bouncy number is a number where the digits are neither strictly increasing nor decreasing.
# Find the number of non-bouncy numbers below a googol

results = {}
results2 = {}

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

def numDecreasing (digits, firstDigit) :
	if digits is 0 :
		return 0
	elif digits is 1:
		return 1
	else :
		try :
			return results2[(digits, firstDigit)]
		except :
			ret = sum([numDecreasing(digits-1, n) for n in range (firstDigit, -1, -1)])
			results2[(digits, firstDigit)] = ret
			return ret

digits = 100
total = 2*numIncreasing(digits+1, 0)
print total

for i in range(2,digits) :
	total += numIncreasing(i+1,0)

print total

total -= 10
for i in range(2,digits) :
	total -= 9
	
print total - digits + 1