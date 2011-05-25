# Find the perimeter p < 1000 which has the most integer pythagorean triplets that sum to it

from useful import doubleFactorize

maxP = 0
maxLen = 0

for p in range(1000) :
	l = doubleFactorize(p)
	if len(l) > maxLen :
		maxLen = len(l)
		maxP = p

print maxP