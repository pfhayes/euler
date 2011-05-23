# Find the sum of all numbers that cannot be written as the sum of two abundant numbers
# An abundant number is a number whose divisors sum to greater than the number
# All numbers greater than 28123 can be written as the sum of two abundant numbers.

# First generate all abundant numbers.
# Taken from Euler21.py

from math import sqrt

divisorSums = {0:0, 1:0, 2:1, 3:1}

def sumDivisors (n) :
	try :
		return divisorSums[n]
	except :
		sum = 1
		for i in range(2, sqrt(n) + 1) :
			if (n%i == 0) :
				if i == n/i :
					sum = sum + i
				else :
					sum = sum + i + n/i
		divisorSums[n] = sum
		return sum
		
abundants = {}

for i in range(28124) :
	if sumDivisors(i) > i :
		abundants[i] = True
	else :
		abundants[i] = False
		
sum = 0
for i in range(28124) :
	print i
	for j in range (i/2 + 1) :
		if abundants[j] == True and abundants[i-j] == True :
			break
	else :
		sum += i
print sum