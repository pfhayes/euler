# Find the number of reduced proper fractions
# where the denominator is less than 1000000

from useful import phi

tot = 0

for i in range(2,1000001) :
	tot += phi(i)
print tot