# Find all numbers that are equal to the sums of their digits.

def fact(n) :
	if n is 1 or n is 0 :
		return 1
	else :
		return n * fact(n-1)

def factSum (n) :
	sum = 0
	while n > 0 :
		sum += fact(n % 10)
		n /= 10
	return sum

sum = 0
for i in range(3,10000000) :
	if factSum(i) == i :
		print i
		sum += i

print sum