# Find the last 10 digits of the non-Mersenne prime 28433*2^7830457+1.

i = 0
num = 1
digs = (10**20)
while (i < 7830457-32) :
	num = (num << 32) % digs
	i+=32

num = (num << (7830457-i))
print 28433*num+1