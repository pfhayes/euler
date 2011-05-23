# See Euler120.py

from useful import PrimeList

primes = PrimeList(2*(10**7))

n = 1
r = 0
while r < 10**10 :
  n += 2
  pn = primes[n-1]
  r = 2 * n * pn

print n, pn, r
