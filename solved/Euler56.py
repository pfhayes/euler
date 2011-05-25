# Find the maximum possible sum of digits for a^b, with a,b < 100

from useful import digits

maxA, maxB, maxSum = 0,0,0

for a in range (100) :
	for b in range(100) :
		s = sum(digits(a**b))
		maxSum = max([s,maxSum])
		if s == maxSum :
			maxA = a
			maxB = b

print maxSum, a, b