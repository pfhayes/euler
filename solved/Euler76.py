# Find the number of ways to write 100 as a sum.

from time import time

def waysToWrite(n,maxblocksize) :
	if maxblocksize == 1:
		return 1
	ret = 0
	if n >= maxblocksize :
		ret += waysToWrite(n - maxblocksize, maxblocksize)
	if maxblocksize > 1 :
		ret += waysToWrite(n,maxblocksize-1)
	return ret
t=time()
print waysToWrite(100,99)
print time()-t