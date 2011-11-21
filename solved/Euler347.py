# Find for all primes p, q, find the largest positive integer M such that
# M = p^e1 * q^e2, where M <= 10000000. Find the sum of all M's.

from useful import PrimeList

top = 10*1000*1000
primes = PrimeList(top)

highest_n = {}
for i in xrange(len(primes)) :
  p = primes[i]
  if p * primes[i+1] > top :
    break
  print p
  for j in xrange(i+1, len(primes)) :
    q = primes[j]
    if p*q > top :
      break

    # Compute all products of the form p^e1 * q^e2 less than top
    # and find the highest product that we get
    e2 = 1
    prod = p*(q**e2)
    while prod <= top :
      while prod * p <= top :
        prod *= p
      highest_n[(p, q)] = max([highest_n.get((p, q), 0), prod])
      e2 += 1
      prod = p*(q**e2)

print sum(highest_n.itervalues())
