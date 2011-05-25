# Find all four "curious" fractions less than 1 with two-digit numerators
# and denominators. A curious fraction is like this:
#	49	 4/
#	-- = --
#	98   /8

top = 1
bottom = 1
for i in range(10,100) :
	for j in range (10,i) :
		if j % 10 == i/10 and j * (i%10) == (j/10) * i :
			top *= j
			bottom *= i
			print str(j) + "/" + str(i)
print str(top) + "/" + str(bottom)