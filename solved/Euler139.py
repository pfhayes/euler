# We want to find all pythagorean triples (x,y,z) with x+y+z < 100 million
# such that y - x divides z

# Generate all primitive pythatgorean triples using the formula
# x = m^2 - n^2, y = 2mn, z = m^2 + n^2
# Then, we will need to consider that scaling by a factor of k forms
# another pythagorean triple with the same property

# This program does not terminate in a timely fashion, because we use a 
# very generous upper bound for m, but it does output the solution within
# 1 minute

from math import sqrt
from useful import gcd

top = 100 * 1000 * 1000

count = 0
for m in xrange(top) :
  if m % 2 == 1 :
    lower = 2
  else :
    lower = 1
  for n in xrange(lower, m, 2) :
    if gcd(m, n) != 1 :
      continue
    x = m*m - n*n
    y = 2*m*n
    z = m*m + n*n

    if z % (x-y) == 0 :
      # For what scaling values of k is k * (x + y + z) < 100 million?
      k = top / (x+y+z)
      count += k
      print (x,y,z), k, count

print count
