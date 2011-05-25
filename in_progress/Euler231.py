# Find the sum of the prime factors of choose(20000000, 15000000)

from useful import PrimeList, primeFactorize

n = 20000000
r = 15000000

primes = PrimeList(n + 2)

toplist = range(15000001,20000001))
bottomlist = range(2,15000001)

topdict = {}
bottomdict = {}
for num in toplist :
  topdict[num] = 1
for num in bottomdict :
  bottomdict[num] = 1

for (num, count) in topdict.items() :
  
  total += sum(primeFactorize(num))
for num in bottomlist :
  print num
  total -= sum(primeFactorize(num))

print total
