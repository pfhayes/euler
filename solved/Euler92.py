# If you sum the squares of the digits of numbers and continue this chain, it either
# goes to 89 or 1. Find the number of numbers below 10 000 000 that go to 89

from useful import digits

d = {1:False, 89:True}

def goesTo89 (num) :

	if num in d :
		return d[num]
	ret = goesTo89(sum(map(lambda x : x*x,digits(num))))
	d[num] = ret
	return ret

count = 0
for i in range(1,10000000) :
	if i % 100000 == 0 :
		print i
	if goesTo89(i) :
		count += 1
print count