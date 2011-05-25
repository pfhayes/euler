# Find the last 10 digits of 1^1 + 2^2 + 3^3 + ... + 1000^1000

sum = 0
for i in range (1,1001) :
	sum += i**i
	
print sum