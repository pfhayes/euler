# Find the number of lengths of wire below 2 000 000
# that can form a right-angled triangle in exactly one way

from useful import gcd
		
oneWay = {}

n = 1
m = 2
while m*m + 2*m*n + m*m <= 2000000 :
	val = 2*m*(m+n)
	while val <= 2000000 :
		if gcd(m,n) == 1 :
			count = 1
			while count*val <= 2000000 :
				if count*val in oneWay :
					oneWay[count*val] = False
				else :
					oneWay[count*val] = True
				count += 1
		m += 2
		val = 2*m*(m+n)
	n += 1
	m = n+1

print len([key for key in oneWay.keys() if oneWay[key] == True])