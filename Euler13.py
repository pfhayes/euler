#Calculate the first ten digits of the sum of 100 50-digit numbers

#Since the later on digits, when summed 100 times will not bubble up to the leading
# digits, we only need to consider the first few digits in our sum.

f = open ("Euler13.txt")

sum = 0
for line in f :
	sum += int(line[0:11])

print sum