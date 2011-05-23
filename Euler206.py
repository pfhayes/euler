# Brute force ahoy!

import time
t= time.time()

"""try :
	for j in xrange(1000000000) :
		k = j
		num = 1020304050607080900
		val = 10
		while j :
			num, j = num + j%10*val, j/10
			val *= 100
		guess = int(num**0.5)
		if num % guess == 0 :
			print num
			print time.time() - t
except :
	print k"""

def test(n) :
	sq = n*n
	for i in reversed(range(10)) :
		sq /= 100
		if sq % 10 != i :
			return False
	return True
	
try :
	for j in xrange(10**8) :
		if test(100*j+30) :
			print 100*j+30
			print time.time() - t
		if test(100*j+70) :
			print 100*j+70
			print time.time() - t
except :
	print j