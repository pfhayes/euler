# The probability that is has happened after the nth iteration
# is

# (1-1/2^n)^bitlen

# The probability that it happens at exactly the nth iteration is
# (1-1/2^n)^bitlen*(1-(1-1/2^(n-1))^bitlen)

import random
from useful import choose

bitlen = 32

# Simulation
"""
n = 0
for i in xrange(1000) :
  x = [0] * bitlen
  count = 0
  while x != [1]*bitlen :
    for i in xrange(len(x)) :
      if random.randint(0,1) == 1 :
        x[i] = 1
    count += 1
  n += count

print n / 1000.0
exit(1)
"""

ev = 0
i = 1
num1s = [0] * (bitlen+1)
num1s[0] = 1
while True :
  lastNum1s = num1s
  num1s = [0]* (bitlen+1)
  for x in xrange(len(num1s)) :
    for j in xrange(x+1) :
      n = bitlen - j
      num1s[x] += lastNum1s[j] * choose(n, x - j) * (1.0 / 2**(n))
  curr = i * (num1s[bitlen] - lastNum1s[bitlen])
  i += 1
  if ev + curr == ev :
    break
  ev += curr
  print ev, curr
