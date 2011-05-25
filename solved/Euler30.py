# Find the sum of all numbers that can be written as the sum of 5th powers of their digits

def fifthSum (n) :
	sum = 0
	while n > 0 :
		sum += (n % 10)**5
		n /= 10
	return sum

sum = 0
for i in range(10000001) :
	if fifthSum(i) == i :
		print i
		sum += i

print sum