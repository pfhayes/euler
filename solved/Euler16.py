# Find the sum of the digits in 2^1000

s = str(2**1000)
sum = 0

for c in s :
	sum += int(c)
print sum