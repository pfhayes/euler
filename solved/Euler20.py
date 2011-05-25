# Find the sum of the digits in 100!

def fact(n) :
	if n is 1 :
		return 1
	else :
		return n * fact(n-1)
		
print sum(int(c) for c in str(fact(100)))