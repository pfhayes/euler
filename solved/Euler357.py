# Find the number of integers n <= 100,000,000 such that for each divisor
# d of n, d + n/d is prime

import math, os, sys
from useful import PrimeList

top = 100 * 1000 * 1000
prime_list = PrimeList(top+1)
primes = set(prime_list)
print 'got primes'

# Observe that, past 2, we should only be concerned with numbers
# congruent to 2 mod 4, since
#   a) If the number is odd, then 1 + n is even and hence not prime
#   b) If the number is divisible by 2, then if n/2 is even, then we
#      have that 2 + n/2 is even and hence not prime

# Furthermore, we do not consider any numbers congruent to 2 mod 3, because
# then we have that 1 + n is divisible by 3.

# Combining these results, the only valid solutions are congruent to either
# 6 or 10 mod 12.

# And, since n + 1 must be prime, only check numbers that are 1 less than
# a prime

s = 3   # Counting 1 and 2
for j in prime_list :
  n = j-1
  if n % 12 == 6 or n % 12 == 10 :
    # Compute divisors. We do this inline so we can break out as soon
    # as we find a divisor that fails to satisfy d + n/d prime
    for f in xrange(1,int(math.sqrt(n))+1) :
      if n % f == 0:
        if f + n/f not in primes :
          break
    else :
      print n
      s += n

print s

