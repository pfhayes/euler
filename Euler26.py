# Find a number d < 1000 such that 1/d has the longest recurring decimal

m = 0
maxLen = 0
for d in range (2,1000) :
	divisor = 1
	quotient = 0
	remainders = []
	while divisor % d != 0 and divisor % d not in remainders:
		quotient += divisor / d
		remainders.append(divisor % d)
		divisor *= 10
	if len(remainders) > maxLen :
		maxLen = len(remainders)
		m = d
		print d, len(remainders)
	
print m