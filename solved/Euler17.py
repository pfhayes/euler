# Find the number of letters required to write each number out from 1 to 1000.

def ones (n) :
	if n is 0 :
		return 0
	if n in [1,2,6] :
		return 3
	if n in [4,5,9] :
		return 4
	if n in [3,7,8] :
		return 5
	raise Exception ("Ones:" + str(n))

def tens (n) :
	if n / 10 is 0 :
		return ones(n)
	if n / 10 is 1 :
		if n in [10] :
			return 3
		if n in [11,12] :
			return 6
		if n in [15,16] :
			return 7
		if n in [13,14,18,19] :
			return 8
		if n is 17 :
			return 9
	if n / 10 in [4,5,6] :
		return 5 + ones(n%10)
	if n / 10 in [2,3,8,9] :
		return 6 + ones(n%10)
	if n / 10 is 7 :
		return 7 + ones(n%10)
	raise Exception ("Tens:" + str(n))

def hundreds (n) :
	if n / 100 in [1,2,3,4,5,6,7,8,9] :
		if n % 100 is 0 :
			return ones(n/100) + len("hundred")
		return ones(n/100) + len("hundredand") + tens(n%100)
	if n / 100 is 0 :
		return tens(n)
	if n / 100 is 10 :
		return len("onethousand")

sum = 0
for i in range(1,1001) :
	sum += hundreds(i)
print sum