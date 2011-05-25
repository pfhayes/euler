# Find the number of Lychrel numbers below 10000

from useful import digits, isPali, digitsToNum

count = 0
for i in range(10000) :
	sum = i
	for j in range(50) :
		l = digits(sum)
		l.reverse()
		sum += digitsToNum(l)
		if isPali(sum) :
			break
	else :
		print i
		count += 1

print count
		