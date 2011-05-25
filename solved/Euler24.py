# Find the millionth lexographic permutation of the digits 0-9

facts = {0:1, 1:1}

def fact(n) :
	try :
		return facts[n]
	except :
		facts[n] = n * fact(n-1)
		return facts[n]

sum = 0
l = [0,1,2,3,4,5,6,7,8,9]
for i in range(10,0,-1) :
	count = 0
	while (count+1) * fact(i-1) + sum <= 999999 and count < i-1:
		count += 1
	sum += count * fact(i-1)
	print l.pop(count) , 