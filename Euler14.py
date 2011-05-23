# Find the longest Collatz chain that starts under 1 000 000.
# Where Tn+1 = n/2 if n is even and 3n+1 if n is odd.

lengths = {0:0, 1:0}
m = 1

def collatz(n) :
	try :
		return lengths[n]
	except :
		if n % 2 == 0 :
			this = collatz (n/2) + 1
		else :
			this = collatz (3*n + 1) + 1
		lengths[n] = this
		return this

for i in range(1*1000*1000) :
	if collatz(i) > collatz(m) :
		print i, collatz(i)
		m = i
print m