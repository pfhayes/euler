# Find the number of values of nCr with n <= 100 such that nCr > 1000000

# Pascal's triangle! We generate the bottom row, and work upwards.

def fact(n) :
	if n == 1 or n == 0:
		return 1
	else :
		return n * fact(n-1)

def choose(n,r) :
	return fact(n)/fact(r)/fact(n-r)

n = 100
l = [choose(n,r) for r in range(51)]

total = 0
while True :
	leftBound = 0
	for i in range(len(l)) :
		if l[i] > 1000000 :
			leftBound = i
			break
	else :
		break
	if n % 2 == 0 :
		total += 2 * len(l[leftBound:]) - 1
		l = [choose(n-1,r) for r in range(leftBound,n/2)]
	else :
		total += 2 * len(l[leftBound:])
		l = [choose(n-1,r) for r in range(leftBound,n/2 + 1)]
	n -= 1

print total