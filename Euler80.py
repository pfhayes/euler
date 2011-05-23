# Compute the irrational square roots of all n in 1 <= n <= 100 to 100 decimal places
	# The answer is the sum of all the decimal digits
	
from math import log10, sqrt
from useful import digits	

s = 0

for square in range(100) :
	if square in [0,1,4,9,16,25,36,49,64,81] :
		continue
	c = square
	p = 0
	x = int(sqrt(square))
	y = (20*p + x)*x
	p = x
	c = c - y
	for times in range(99) :
		c *= 100
		for x in range(11) :
			y = (20*p + x)*x
			if y > c :
				x -= 1
				y = (20*p + x)*x
				p = 10*p + x
				break
		c = c - y
	s += sum(digits(p))

print s