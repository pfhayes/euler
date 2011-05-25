# By summing the factorials of the digits, and repeating, we get a loop
# How many numbers below 1000000 form loops of exactly 60 terms?

from useful import fact
manies = {}

def howMany(n) :
	try :
		return manies[n]
	except :
		sum = 0
		i = n
		manies[n]=0
		while n :
			sum += fact(n%10)
			n /= 10
		manies[i] = 1 + howMany(sum)
		return manies[i]
count = 0
for i in range(1,1000000) :
	if howMany(i) == 60 :
		count += 1
		
print count