# Find the first iteration where the ratio of primes along th diagonals
# of a spiral is below 10%. The spiral is formed as follows:
#	21	22	23	24	25	...
#	20	7	8	9	10
#	19	6	1	2	11
#	18	5	4	3	12
#	17	16	15	14	13

from useful import PrimeDict, isPrime

total = 0
primes = 0
it = 0
side = 1

while it == 0 or primes*10.0 / total >= 1 :
	#print it, primes, total
	it += 1
	side += 2
	
	if isPrime(side**2 - side + 1):
		primes += 1
	if isPrime((2*it)**2 + 1):
		primes += 1
	if isPrime((2*it)**2 - 2*it + 1):
		primes += 1
	total += 4

print side - 2