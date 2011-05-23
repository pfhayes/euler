# Find the first triangle number with over 500 divisors.

# Description: First note that the nth triangle number is n*(n+1)/2
#				Then note that if x = yz, and x, y, z are integers, then
#				numDivisors(x) = numDivisors(y) * numDivisors(z)
#				So, we have a factoring of the nth triangle number, and we
#				determine the number of divisors of each factor and then multiply

divisors = {1:1, 2:2, 3:2}

def numDivisors (n) :
	try :
		return divisors[n]
	except :
		count = 2
		for i in range(2, n/2+1) :
			if (n%i == 0) :
				count = count + 1
		divisors[n] = count
		return count

count = 1
m = 1
while True :
	num1 = count
	count = count + 1
	num2 = count
	if num1 %2 is 0 :
		num1 = num1 / 2
	else:
		num2 = num2 / 2 
	tot = numDivisors(num1) * numDivisors(num2)
	if tot > m :
		print tot
		m = tot
	if tot >= 500 :
		print num1 * num2
		break		
	#print num1*num2, numDivisors(num1) * numDivisors(num2)
	
#print divisors