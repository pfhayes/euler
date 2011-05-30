# Find the first number that can be written as a sum or primes in over 5000
# different ways

# Use an algorithm similar to problem 76

from useful import PrimeList

primes = PrimeList(5000)

memoized = {}

def waysToWrite(n, maxblocksize_index) :
  if maxblocksize_index == 0 :
    return n % primes[maxblocksize_index] == 0
  if ((n, maxblocksize_index) in memoized) :
    return memoized[(n, maxblocksize_index)]
  ret = 0
  if n >= primes[maxblocksize_index] :
    ret += waysToWrite(n - primes[maxblocksize_index], maxblocksize_index)
  if maxblocksize_index > 0 :
    ret += waysToWrite(n, maxblocksize_index - 1)
  memoized[(n, maxblocksize_index)] = ret
  return ret

current_prime_index = 0
n = 2
nextprime = primes[current_prime_index + 1]
while True :
  if waysToWrite(n, current_prime_index) >= 5000 :
    print n
    break
  if n >= nextprime :
    current_prime_index += 1
    nextprime = primes[current_prime_index + 1]
  n += 1

