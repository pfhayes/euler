# Find the smallest number x such that x, 2x, 3x, 4x, 5x, and 6x contain the same digits.

def digList (n) :
	s = [c for c in str(n)]
	s.sort()
	return s

p = 100
stop = False
while True :
	print p
	for i in range(p, 10*p/6) :
		l = digList(i)
		if l == digList(2*i) and l == digList(3*i) and l ==digList(4*i) and l == digList(5*i) and l ==digList(6*i) :
			print i, digList(i)
			stop = True
			break
	if stop :
		break
	p *= 10