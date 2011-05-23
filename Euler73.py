# Find the number of fractions that lie between 1/3 and 1/2 in a sorted list
# of reduced proper fractions

d = {}

def gcd(a,b) :
	if (a,b) in d :
		return d[(a,b)]
	else :
		if b == 0 :
			return a
		return gcd(b, a%b)

lowest = (1,3)
highest = (1,2)

total = 0
for denom in range(2,10001) :
	print denom
	start = denom / 3 + 1
	stop = denom / 2
	for i in range(start, stop+1) :
		if gcd(i,denom) != 1 :
			continue
		total +=1

print total-1 # Because it includes 1/2