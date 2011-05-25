from useful import PrimeList

primes = PrimeList(10**7+260)
prime_set = set(primes)

def numDivisors(n) :
  if n in prime_set :
    return 2
  ret = 1
  for f in primes :
    if f > n :
      return ret
    while n % f == 0 :
      n = n/f
      ret += 1
  return ret

tot = 0
last = 1
num = 2
while num < 10**3 :
  nd = numDivisors(num)
  if nd == last :
    tot += 1
    print num, num-1
  last = nd
  num += 1

print tot
