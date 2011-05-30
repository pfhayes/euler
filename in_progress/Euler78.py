# Find the number of ways to split n councs into any number of piles

# Define M(n, k) to be the number of ways to split n coins into 
# piles of no more than k coins.

d = {}
d[(1,1)] = 1

def M(n, k) :
  if n <= 1 :
    return 1
  if k == 1 :
    return 1
  if (n,k) in d :
    return d[(n,k)]
  total = 0
  for i in xrange(1, k+1) :
    if i > n :
      break
    total += M(n-i, i)
  d[(n,k)] = total
  return total

i = 4
largest_pow = 10
while True :
  res = M(i,i)
  if res % largest_pow == 0 :
    print i, largest_pow, res
    largest_pow *= 10
  i += 5
