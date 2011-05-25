# Find the number of values of N <= 10000 for which sqrt(N) has an odd period.

import math
count = 0

for i in range(1,4) :
	lowest = i**2 + 1
	for j in range (lowest,(i+1)*(i+1)) :
	#for j in range(151,152) :
		print j
		terms = []
		first = i
		#first = 12
		num = j
		exact = math.sqrt(num)
		top = 1
		bottomright = first
		term = (top, bottomright)
		exp = [first]
		tries = 0
		while term not in terms and tries < 100 :
			topTup = (top,bottomright)
			#exact = 1/(exact-first)
			#first = int(math.floor(exact))
			exp.append(first)
			terms.append(term)
			oldbottom = num - bottomright*bottomright
			if oldbottom % topTup[0] != 0 :
				print bottom, topTup
				print "ERROR"
				print num
				print terms
				print exp
				quit()
			bottom = oldbottom / topTup[0]
			bottomright = bottom * first - topTup[1]
			top = bottom
			term = (top, bottomright)
			first = int(math.floor(((exact + bottomright)/top)))
			#print tries+1,first,bottom,bottomright, top,topTup
			tries += 1
		print exp
		if tries == 100 :
			print bottom, topTup
			print "ERROR"
			print num
			print terms
			print exp
			quit()
		elif (len(exp) - 1) % 2 == 1 :
			count += 1
print count