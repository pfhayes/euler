# In the fractional expansion of sqrt(2), find the number of terms below 1000 where
# the numerator has more digits than the denominator

from math import log10

num = 3
den = 2
count = 0

for i in range(1000) :
	num += den
	num, den = den, num
	num += den
	if int(log10(num)) > int(log10(den)) :
		print num, den
		count += 1

print count