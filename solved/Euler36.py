# Find all numbers less than one million that are palindromic in base 10 and base 2

def oddPalify(n) :
	return int(str(n) + str(n)[:-1][::-1])
	
def evenPalify(n) :
	return int(str(n) + str(n)[::-1])

def bin(n) :
	st = ""
	while n > 0 :
		if n % 2 :
			st = "1" + st
		else :
			st = "0" + st
		n /= 2
	return st

def isPali(st) :
	st = str(st)
	for i in range(len(st)/2+1) :
		if st[i] != st[-i-1] :
			return False
	return True

sum = 0

for x in range (1,1000) :
	pali1 = evenPalify(x)
	pali2 = oddPalify(x)
	if isPali(pali1) :
		binStr1 = bin(pali1)
		if isPali(binStr1) :
			print pali1, binStr1
			sum += pali1
	if isPali(pali2) :
		binStr2 = bin(pali2)
		if isPali(binStr2) :
			print pali2, binStr2
			sum += pali2
print sum