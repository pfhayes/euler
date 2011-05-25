# Count the number of squarefrees below 2^50

# Strip all the multiples of 4, 9, 16, etc.
# Then, we double counted all the multiples of 4*9, 9*16, etc.
# Repeat until we got everything

import math
from useful import PrimeList

start = 2**50
total = start

primes = PrimeList(int(math.sqrt(start))+100)

for p in primes :
  total -= start / (p*p)

# After first pass
print total

doubles = []

# Remove double counts
for i in xrange(len(primes)) :
  p1 = primes[i]
  sq = p1*p1
  for j in xrange(i+1, len(primes)) :
    p2 = primes[j]
    tot = sq*p2*p2
    if tot > start :
      break
    total += start / tot
    doubles.append((p1,p2))

# After second pass
print total

# Subsequent passes
groups = doubles
add_or_sub = -1
while len(groups) > 0 :
  print groups[0:5]
  new_groups = []
  for i in xrange(len(groups)) :
    print i
    g1 = groups[i]
    lis1 = list(g1)
    prod = 1
    for x in g1 :
      prod *= x*x
    for j in xrange(i+1, len(groups)) :
      g2 = groups[j]
      tot = prod
      lis2 = list(lis1)
      for x in g2 :
        if x not in g1 :
          tot *= x*x
          lis2.append(x)
      if tot > start :
        break
      new_groups.append(lis2)
      total += (add_or_sub) * (start / tot)
  add_or_sub *= -1
  groups = new_groups
  print total


