# Find the sum of the distinct squarefree numbers in the first 51 rows of
# Pascal's triangle

from useful import PrimeList, choose

primes = PrimeList(10**6)

def squarefree(n) :
  for prime in primes :
    if prime > n :
      return True
    if n % prime == 0 :
      if (n / prime) % prime == 0 :
        return False
      n = n / prime
  return True

se = set([])

row_up_to = 51
for j in xrange(row_up_to) :
  for i in xrange(j/2 + 1) :
    num = choose(j, i)
    if (squarefree(num)) :
      se.add(num)

print sum(se)
