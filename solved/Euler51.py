# If we replace the *'s in 56**3 with the same digit, we get seven primes. Namely,
# 56003, 56113, 56333, 56443, 56663, 56773, 56993. Find the smallest element of the 
# first eight prime family. Not necessarily adjacent digits.

# It must be a set of digits that is of length of a multiple of 3. Otherwise, at least
# 3 of the entries will be multiples of 3.

from useful import PrimeList, digitsToNum

primes = PrimeList(1000000)

print "Done primes!"

# Tried 5-digit numbers... didn't work.
# Contruct all 6-digit numbers that have 3 digits in common.
numdigs = 6
for i in range(10) :
	for j in range(10) :
		for l in range(10):
			for pos1 in range(numdigs) :
				for pos2 in range(numdigs) :
					for pos3 in range(numdigs) :
						numcomps = 0
						digs = []
						for k in range(10) :
							digs = [k for x in range(numdigs)]
							digs[pos1] = i
							digs[pos2] = j
							digs[pos3] = l
							if digs[0] == 0 or digitsToNum(digs) not in primes :
								numcomps += 1
							if numcomps > 2 :
								break
						if numcomps <= 2:
							print pos1, i, pos2, j, pos3, l, digs
	
print "Done!"