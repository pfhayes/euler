# Find the number of ways to split n councs into any number of piles
# Recursively compute the nth partition number using a more efficient method
# Adapted from http://mathworld.wolfram.com/PartitionFunctionP.html

import math

d = {}
d[0] = 1

def P(n) :
  if (n < 0) :
    return 0
  if n in d :
    return d[n]

  total = 0
  for k in xrange(1, math.sqrt(n)+1) :
    val1 = P(n - k * (3 * k - 1) / 2)
    val2 = P(n - k * (3 * k + 1) / 2)

    if (k % 2 == 1) :
      total += val1 + val2
    else :
      total -= val1 + val2

  d[n] = total
  return total

# We make the optimizing observation that the result can only be divisible
# by a power of 10 for i % 10 == 4 or 9
i = 4
largest_pow = 10
while True :
  res = P(i)
  if res % largest_pow == 0 :
    print i, largest_pow, res
    largest_pow *= 10
  i += 5
