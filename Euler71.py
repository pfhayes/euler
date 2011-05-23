# In a sorted list of all reduced proper fractions where the denominator <= 1000000,
# find the fraction to the left of 3/7

from useful import gcd

lowest = (2,7)

for denom in range(2,1000001) :
	if denom == 7:
		continue
	x = 3 * denom / 7
	while (x+1)*7 < 3*denom :
		x += 1
	if gcd(x,denom) != 1 :
		continue
	if lowest[1] * x > lowest[0] * denom :
		lowest = (x,denom)

print lowest