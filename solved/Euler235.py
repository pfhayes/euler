#!/usr/bin/env python

# Define u(k) = (900 - 3k)*r^k-1
# Define s(n) = sum from 1 to n of u(k)

# Find the value of r for which s(5000) = -600,000,000,000

def u(k, r) :
  return (900 - 3*k)*r**(k-1)
def s2(n, r) :
  return sum(map(lambda x : u(x, r), xrange(1, n+1)))
s = lambda r : s2(5000, r)
target = -600*1000*1000*1000

# Binary search on values of r
bottom = 1.0
top = 1.1
last = None
while bottom < top :
  mid = (bottom + top)/2
  curr = s(mid)
  if curr == last :
    break
  if (curr < target) :
    top = mid
  else :
    bottom = mid
  last = curr

print format(mid, '.12f')

