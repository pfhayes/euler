#Find the sum of the perimeters of all almost equilateral triangles
# with perimeters less than 1 000 000 000

from math import sqrt

print "Ready"

tot = 0
for i in xrange(2,400000000) :
	if not i % 100000 :
		print i
	# Tri1
	per1 = 3*i - 1
	s = per1/2
	a = (s*(s-i)*(s-i)*(s-i+1))
	p = a**0.5
	if int(p)**2 == a :
		print (i,i,i-1)
		tot+=per1
	per2 = 3*i + 1
	s = per2/2
	a = (s*(s-i)*(s-i)*(s-i-1))
	p = a**0.5
	if int(p)**2 == a :
		print(i,i,i+1)
		tot+=per2

print tot