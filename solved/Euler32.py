# Find all numbers x that can be factored into x=ab such that x, a, and b contain each digit 1 through 9 exactly once.

# Let us generate all 4 or 5-digit numbers that are composed of unique digits.

from useful import primeFactorize, digits
				
sum = 0
for i in range (1000, 10000) :
	dList = digits(i)
	if (len(set(dList)) != len(dList) or 0 in dList) :
		continue
	factors = primeFactorize(i)
	for j in range(2**len(factors)) :
		num1 = 1
		num2 = 1
		for k in range(len(factors)) :
			if j/(k+1) == 1 :
				num1 *= factors[k]
			else :
				num2 *= factors[k]
		allDigits = dList + digits(num1) + digits(num2)
		if (len(allDigits) == 9 and len(set(allDigits)) == 9 and 0 not in allDigits) :
			print i, num1, num2, "!"
			sum += i
			break

print sum