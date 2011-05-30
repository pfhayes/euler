# Find the number of Hamming numbers of type 100 that are <= 10^9
# A Hamming number of type 100 has no prime factors above 100

# So, we want the number of solutions to 2^a1 * 3^a2 * ... * 100^an <= 10^9
# => a1*log2 + a2*log3 + ... + an*log100 <= 9

from math import log
from useful import PrimeList

type = 100
primes = PrimeList(type+1)
logs = map(log, primes)

top = 10**9

def numsols(lessthan, length) :
  if length == 1 :
    return int(lessthan / logs[0]) + 1
  ret = 0
  for i in xrange(int(lessthan / logs[length-1]) + 1) :
    ret += numsols(lessthan - i * logs[length - 1], length - 1)
  return ret
  
print numsols(log(top), len(primes))
