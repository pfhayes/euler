# Find the value of D which gives the largest minimal solution
# in x for x^2 - Dy^2 = 1

from math import sqrt

cands = [x for x in range(1001) if int(sqrt(x))**2 != x]
left = len(cands)

x = 2
while left > 1 :
	Dy2 = x*x - 1
	toBeDiscarded = 0
	for i in xrange(len(cands)) :
		cand = cands[i]
		if cand and Dy2 % cand == 0:
			y2 = Dy2 / cand
			sqTest = int(y2**0.5)
			if y2 % sqTest == 0 and y2 /sqTest == sqTest :
				toBeDiscarded += 1
				cands[i] = 0
	if toBeDiscarded :
		left -= toBeDiscarded
		print "At x="+str(x)+", discarding", toBeDiscarded, left
	x += 1

print cands