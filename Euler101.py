# Find succesive polynomial approximations to a 10th degree polynomial

from numpy import *

def getPoly(n) :
	def u(x) :
		ret = 0
		for i in range(n+1) :
			ret += (-1)**i * x**i
		return ret
	
	def g(x) :
		return x**3
	return u

u10 = getPoly(10)

terms = [u10(x) for x in range(1,11)]
print terms
st = 0

for i in range(1,len(terms)+1) :
	sublist = terms[:i]
	#print sublist
	# Model a polynomial to the terms in sublist!
	l = []
	for j in range(len(sublist)) :
		l.append([(x+1)**(j) for x in range(i)])
	M = transpose(array(l, dtype=int64))
	arr = array([[x] for x in sublist], dtype=int64)
	#print M
	#print arr
	coeffs = linalg.solve(M,arr)
	#print coeffs
	s = 0
	m = len(sublist)+1
	for j in range(len(coeffs)) :
		s += coeffs[j][0] * m**j
	#print s
	st += s
print st