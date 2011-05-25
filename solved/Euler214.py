from useful import PrimeList

top = 40000000
length = 25

primes = PrimeList(top)

chains = [-1 for x in xrange(top+1)]

chains[0] = 1
chains[1] = 1

def primeFactorize (n) :
  ret = []
  for p in primes :
    while n % p == 0 :
      ret.append(p)
      n /= p
    if n == 1 :
      return ret
  return ret + [n]

def phi(n) :
	facts = primeFactorize(n)
	if len(facts) == 1:
		return n - 1
	return n * reduce(lambda x,y:x*y, [float(fact - 1)/fact for fact in set(facts)])

def getChains(p) :
  if chains[p] == -1 :
    chains[p] = getChains(int(phi(p)+0.5)) + 1
  return chains[p]

for p in primes :
  print p
  chains[p] = getChains(p-1) + 1

count = 0
for p in primes :
  n = chains[p]
  if n == length :
    count += p
print count
