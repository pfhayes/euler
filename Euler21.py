# Calculate the sum of all amicable numbers under 10 000
# Two numbers a and b are amicable if sumDivisors(a) = b
# and sumDivisors(b) = a, a=/= b

# Check out Euler 12.py for stuff about divisors

divisorSums = {0:0, 1:0, 2:1, 3:1}

def sumDivisors (n) :
	try :
		return divisorSums[n]
	except :
		sum = 1
		for i in range(2, n/2+1) :
			if (n%i == 0) :
				sum = sum + i
		divisorSums[n] = sum
		return sum

for i in range(30*1000) :
	sumDivisors(i)

sum = 0
for i in range(10*1000) :
	if divisorSums[divisorSums[i]] == i and divisorSums[i] != i :
		sum += i
		if divisorSums[i] < 10*1000 :
			sum += divisorSums[i]
		
print sum/2