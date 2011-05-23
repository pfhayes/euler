# Find the number of characters saved by writing each of the roman numerals in
# the text file in minimal form.

def letToNum(c) :
	if c is "I" :
		return 1
	if c is "V" :
		return 5
	if c is "X" :
		return 10
	if c is "L" :
		return 50
	if c is "C" :
		return 100
	if c is "D" :
		return 500
	if c is "M" :
		return 1000

def parseRoman(n) :
	i = 0
	sum = 0
	while (i < len(n)) :
		if i+1 < len(n) and letToNum(n[i]) < letToNum(n[i+1]) :
			sum += letToNum(n[i+1]) - letToNum(n[i])
			i+=1
		else :
			sum += letToNum(n[i])
		i+=1
	return sum

def minRoman(n) :
	c = []
	while n > 1000 :
		c.append("M")
		n -= 1000
	while n >= 900 :
		c.extend(["C","M"])
		n -= 900
	while n >= 500 :
		c.append("D")
		n -= 500
	while n >= 400 :
		c.extend(["C","D"])
		n -= 400
	while n >= 100 :
		c.append("C")
		n -= 100
	while n >= 90 :
		c.extend(["X","C"])
		n -= 90
	while n >= 50 :
		c.append("L")
		n -= 50
	while n >= 40 :
		c.extend(["X","L"])
		n -= 40
	while n >= 10 :
		c.append("X")
		n -= 10
	while n >= 9 :
		c.extend(["I","X"])
		n -= 9
	while n >= 5 :
		c.append("V")
		n -= 5
	while n >= 4 :
		c.extend(["I","V"])
		n -= 4
	while n >= 1 :
		c.append("I")
		n -= 1
	print c
	return c

s = 0	
ms = 0
for line in open("Euler89.txt") :
	s += len(line.strip())
	ms += len(minRoman(parseRoman(line.strip())))

print s - ms